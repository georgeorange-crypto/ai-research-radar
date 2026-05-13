from __future__ import annotations

from typing import Any, Dict, List, Optional

from .base import BaseModel
from .client import ChatModelClient, log_model_error
from .summary_model import ACTION_CHOICES, SUMMARY_FIELDS


ROLE_ORDER = ["technical_extractor", "relevance_judge", "critic", "editor"]
ROLE_LABELS = {
    "technical_extractor": "Technical Extractor",
    "relevance_judge": "Relevance & Priority Judge",
    "critic": "Critic / Grounding Auditor",
    "editor": "Final Editor",
}

TIER_ORDER = ["IGNORE", "ARCHIVE", "WATCH", "SKIM", "MUST_READ"]
TIER_TO_ACTION = {
    "MUST_READ": "read_pdf",
    "SKIM": "skim",
    "WATCH": "watch",
    "ARCHIVE": "archive",
    "IGNORE": "ignore",
}
ACTION_TO_TIER = {
    "read_pdf": "MUST_READ",
    "skim": "SKIM",
    "watch": "WATCH",
    "save": "ARCHIVE",
    "archive": "ARCHIVE",
    "ignore": "IGNORE",
}
OPEN_SOURCE_ACTIONS = {"study_code", "clone_and_run", "read_readme", "use_as_baseline", "save", "archive"}
GROUNDING_LEVELS = {"title_only", "abstract_only", "full_text", "repo_readme"}
SUMMARY_PLUS_FIELDS = SUMMARY_FIELDS + [
    "primary_category",
    "secondary_tags",
    "reading_tier",
    "quality_notes",
]


TECHNICAL_PROMPT = """你是 Technical Extractor，只负责从 evidence 中抽取技术事实。
不要判断是否值得读，不要写漂亮摘要，不做排名。
只允许使用 evidence 中能看到的信息；缺失就写“未提供”。
返回严格 JSON，字段必须且只能包含：
task, problem, method, experiments_or_benchmarks, claimed_results, limitations, missing_details, evidence_level。"""

RELEVANCE_PROMPT = """你是 Relevance & Priority Judge，只负责判断条目与 George 研究地图的关系和阅读优先级。
George 的核心方向：
- Context Compression / Long Context / Agent Memory
- LLM Agents / Tool Use / Planning / Agentic RL
- Novel Class Discovery / Open-World Learning / OOD / Continual Learning
- Model Distillation / Model Compression / Efficient Training
传统关注：CV, NLP, RL, Model Architecture, Learning Methods。
防止关键词漂移；如果只是泛 Agent、泛 benchmark 或泛开源工具，要降级。
返回严格 JSON，字段必须且只能包含：
primary_category, secondary_tags, relevance_to_user, reading_tier_candidate, suggested_action_candidate, why_for_george, risk_of_topic_drift。"""

CRITIC_PROMPT = """你是 Critic / Grounding Auditor，只负责挑错和质检。
检查 unsupported claims、关键词误命中、source authority 过度加权、reading_tier 与 suggested_action 冲突、分类错误、媒体夸大。
不要重写摘要。
返回严格 JSON，字段必须且只能包含：
unsupported_claims, hype_risk, category_risk, ranking_risk, action_tier_conflict, source_quality_warning, should_downgrade, should_upgrade, critic_notes。"""

EDITOR_PROMPT = """你是 Final Editor，负责把三个角色输出综合成最终日报条目。
必须遵守：
1. 技术事实只能来自 Technical Extractor。
2. 阅读优先级主要参考 Relevance Judge。
3. 如果 Critic 标记 high risk，必须降级或写明不确定。
4. action 必须和 reading_tier 一致。
5. 不允许编造 evidence 中不存在的具体数字、模型名、benchmark 结果。
6. 不允许复读英文 abstract。
7. 不允许使用“主要线索：xxx”这种关键词 fallback 作为最终摘要。
返回严格 JSON，字段必须且只能包含：
what_is_it, problem, method_or_contribution, why_important, deep_read, primary_category, secondary_tags, reading_tier, suggested_action, quality_notes。"""


class RolePipeline(BaseModel):
    """Role-based multi-model research review pipeline."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.roles_config = config.get("roles", {}) if isinstance(config.get("roles"), dict) else {}
        self.clients = self._load_role_clients()

    def _load_role_clients(self) -> dict[str, ChatModelClient]:
        clients: dict[str, ChatModelClient] = {}
        for role in ROLE_ORDER:
            role_config = self.roles_config.get(role, {})
            if not isinstance(role_config, dict):
                continue
            provider = role_config.get("provider") or role_config.get("type") or role
            client = ChatModelClient(
                provider=provider,
                api_key=role_config.get("api_key") or "",
                base_url=role_config.get("base_url") or "",
                model=role_config.get("model") or "",
            )
            if client.configured:
                clients[role] = client
        return clients

    @property
    def available(self) -> bool:
        return all(role in self.clients for role in ROLE_ORDER)

    def summarize(self, item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if not self.available:
            return None

        role_status: dict[str, dict[str, Any]] = {}
        evidence = self._build_evidence(item)
        technical = self._call_role(
            "technical_extractor",
            TECHNICAL_PROMPT,
            {
                "evidence": evidence,
                "required_json": {
                    "task": "...",
                    "problem": "...",
                    "method": "...",
                    "experiments_or_benchmarks": "...",
                    "claimed_results": "...",
                    "limitations": "...",
                    "missing_details": "...",
                    "evidence_level": "title_only/abstract_only/full_text/repo_readme",
                },
            },
            {"task", "problem", "method", "evidence_level"},
            role_status,
        )
        if technical is None:
            self._store_role_metadata(item, role_status, None)
            return None

        relevance = self._call_role(
            "relevance_judge",
            RELEVANCE_PROMPT,
            {
                "evidence": evidence,
                "technical_extractor": technical,
                "current_rule_scores": item.get("scores", {}),
                "current_rule_tier": item.get("reading_tier"),
                "required_json": {
                    "primary_category": "...",
                    "secondary_tags": [],
                    "relevance_to_user": {
                        "context_compression_memory": 0.0,
                        "agents": 0.0,
                        "open_world_learning": 0.0,
                        "model_distillation": 0.0,
                        "rl": 0.0,
                    },
                    "reading_tier_candidate": "MUST_READ/SKIM/WATCH/ARCHIVE/IGNORE",
                    "suggested_action_candidate": "read_pdf/skim/watch/save/use_as_eval/study_code/read_readme/archive/ignore",
                    "why_for_george": "...",
                    "risk_of_topic_drift": "low/medium/high",
                },
            },
            {"primary_category", "reading_tier_candidate", "suggested_action_candidate", "why_for_george"},
            role_status,
        )
        if relevance is None:
            self._store_role_metadata(item, role_status, {"technical_extractor": technical})
            return None

        critique = self._call_role(
            "critic",
            CRITIC_PROMPT,
            {
                "evidence": evidence,
                "technical_extractor": technical,
                "relevance_judge": relevance,
                "current_rule_scores": item.get("scores", {}),
                "current_rule_tier": item.get("reading_tier"),
                "required_json": {
                    "unsupported_claims": [],
                    "hype_risk": 0.0,
                    "category_risk": "low/medium/high",
                    "ranking_risk": "low/medium/high",
                    "action_tier_conflict": False,
                    "source_quality_warning": "",
                    "should_downgrade": False,
                    "should_upgrade": False,
                    "critic_notes": "...",
                },
            },
            {"unsupported_claims", "hype_risk", "category_risk", "ranking_risk", "critic_notes"},
            role_status,
        )
        if critique is None:
            self._store_role_metadata(item, role_status, {"technical_extractor": technical, "relevance_judge": relevance})
            return None

        final = self._call_role(
            "editor",
            EDITOR_PROMPT,
            {
                "evidence": evidence,
                "technical_extractor": technical,
                "relevance_judge": relevance,
                "critic": critique,
                "current_rule_scores": item.get("scores", {}),
                "current_rule_tier": item.get("reading_tier"),
                "required_json": {
                    "what_is_it": "...",
                    "problem": "...",
                    "method_or_contribution": "...",
                    "why_important": "...",
                    "deep_read": "...",
                    "primary_category": "...",
                    "secondary_tags": [],
                    "reading_tier": "MUST_READ/SKIM/WATCH/ARCHIVE/IGNORE",
                    "suggested_action": "read_pdf/skim/watch/save/use_as_eval/study_code/read_readme/archive/ignore",
                    "quality_notes": "...",
                },
            },
            set(SUMMARY_PLUS_FIELDS),
            role_status,
        )
        if final is None:
            self._store_role_metadata(
                item,
                role_status,
                {"technical_extractor": technical, "relevance_judge": relevance, "critic": critique},
            )
            return None

        final = self._apply_deterministic_constraints(item, final, relevance, critique)
        role_payload = {
            "technical_extractor": technical,
            "relevance_judge": relevance,
            "critic": critique,
            "editor": final,
        }
        self._store_role_metadata(item, role_status, role_payload)
        item["_cached_summary"] = {field: final.get(field, "") for field in SUMMARY_FIELDS}
        return final

    def rank(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return sorted(items, key=self._rank_key, reverse=True)

    def _call_role(
        self,
        role: str,
        system_prompt: str,
        user_payload: dict[str, Any],
        required_fields: set[str],
        role_status: dict[str, dict[str, Any]],
    ) -> Optional[dict[str, Any]]:
        client = self.clients.get(role)
        status = {
            "provider": client.provider if client else None,
            "model": client.model if client else None,
            "success": False,
            "error": None,
        }
        role_status[role] = status
        if client is None:
            status["error"] = "not_configured"
            return None

        parsed = client.call_json(system_prompt=system_prompt, user_payload=user_payload, temperature=0.15)
        if parsed is None:
            status["error"] = "empty_or_unparseable_response"
            return None
        missing = sorted(field for field in required_fields if field not in parsed)
        if missing:
            status["error"] = f"missing_fields: {', '.join(missing)}"
            log_model_error(client.provider, client.model, client.base_url, "n/a", status["error"])
            return None
        status["success"] = True
        return parsed

    def _build_evidence(self, item: Dict[str, Any]) -> dict[str, Any]:
        metadata = item.get("metadata") if isinstance(item.get("metadata"), dict) else {}
        source = item.get("source", {}) if isinstance(item.get("source"), dict) else {}
        readme = ""
        for key in ["repo_readme_summary", "readme_summary", "readme_excerpt"]:
            if metadata.get(key):
                readme = str(metadata.get(key))
                break
        evidence_level = self._grounding_level(item, readme)
        return {
            "title": item.get("title"),
            "abstract_or_full_text": item.get("abstract") or item.get("summary") or "",
            "repo_readme": readme,
            "source": source,
            "url": item.get("url"),
            "metadata": metadata,
            "grounding_level": evidence_level,
            "primary_section": item.get("primary_section", {}),
            "primary_category": item.get("primary_category", {}),
            "secondary_tags": item.get("secondary_tags", []),
            "matched_sections": item.get("matched_sections", []),
            "matched_focus_areas": item.get("matched_focus_areas", []),
            "matched_keywords": item.get("matched_keywords", []),
            "scores": item.get("scores", {}),
            "reading_tier": item.get("reading_tier"),
            "is_open_source_project": item.get("is_open_source_project", False),
            "is_benchmark": self._is_benchmark_item(item),
        }

    def _grounding_level(self, item: Dict[str, Any], readme: str) -> str:
        existing = str(item.get("grounding_level") or "").strip()
        if existing in GROUNDING_LEVELS:
            return existing
        if self._is_repository_item(item):
            return "repo_readme" if readme else "title_only"
        if not str(item.get("abstract") or item.get("summary") or "").strip():
            return "title_only"
        source_type = str(item.get("source", {}).get("type", "")).lower()
        if source_type in {"arxiv", "openreview", "hf_daily_papers", "hf_papers_page"}:
            return "abstract_only"
        return "full_text"

    def _apply_deterministic_constraints(
        self,
        item: Dict[str, Any],
        final: dict[str, Any],
        relevance: dict[str, Any],
        critique: dict[str, Any],
    ) -> dict[str, Any]:
        final = dict(final)
        rule_tier = self._normalize_tier(item.get("reading_tier"))
        tier = self._normalize_tier(final.get("reading_tier") or relevance.get("reading_tier_candidate") or item.get("reading_tier"))
        action = self._normalize_action(final.get("suggested_action") or relevance.get("suggested_action_candidate"))

        if tier == "MUST_READ" and rule_tier != "MUST_READ":
            tier = "SKIM"
        if self._critic_blocks_must_read(critique, item) and tier == "MUST_READ":
            tier = "SKIM"
        elif self._should_downgrade(critique) and tier != "IGNORE":
            tier = self._downgrade_tier(tier)
        elif critique.get("should_upgrade") is True and tier not in {"MUST_READ", "IGNORE"}:
            tier = self._upgrade_tier(tier)

        if item.get("reading_tier") == "MUST_READ" and tier == "MUST_READ":
            action = "read_pdf"
        elif tier in TIER_TO_ACTION:
            action = TIER_TO_ACTION[tier]

        if self._is_benchmark_item(item) and action in {"skim", "watch", "save"}:
            item["secondary_action"] = "use_as_eval"
        if self._is_repository_item(item):
            action = action if action in OPEN_SOURCE_ACTIONS else "read_readme"
            tier = action
        elif self._grounding_level(item, "") == "title_only" and action == "read_pdf":
            action = "save"
            tier = "ARCHIVE"

        if action not in ACTION_CHOICES:
            action = TIER_TO_ACTION.get(tier, "save")

        final["reading_tier"] = tier
        final["suggested_action"] = action
        item["role_pipeline_tier"] = tier
        item["role_pipeline_action"] = action
        if tier in {"MUST_READ", "SKIM", "WATCH", "ARCHIVE", "IGNORE"}:
            item["reading_tier"] = tier
            item["worth_deep_read"] = tier == "MUST_READ"
        if final.get("quality_notes"):
            item["quality_notes"] = final.get("quality_notes")
        return final

    def _critic_blocks_must_read(self, critique: dict[str, Any], item: Dict[str, Any]) -> bool:
        source_warning = str(critique.get("source_quality_warning") or "").lower()
        source_type = str(item.get("source", {}).get("kind") or "").lower()
        metadata = item.get("metadata") if isinstance(item.get("metadata"), dict) else {}
        url_text = " ".join([str(item.get("url", "")), str(metadata.get("paper_link", ""))]).lower()
        has_primary_paper = any(hint in url_text for hint in ["arxiv.org", "openreview.net", "doi.org", "paper"])
        return (
            str(critique.get("category_risk") or "").lower() == "high"
            or bool(critique.get("unsupported_claims"))
            or (source_warning == "media_only" and not has_primary_paper)
            or (source_type == "media" and not has_primary_paper)
        )

    def _should_downgrade(self, critique: dict[str, Any]) -> bool:
        try:
            hype_risk = float(critique.get("hype_risk") or 0.0)
        except (TypeError, ValueError):
            hype_risk = 0.0
        return bool(critique.get("should_downgrade")) or hype_risk > 0.6 or str(critique.get("ranking_risk") or "").lower() == "high"

    def _normalize_tier(self, tier: Any) -> str:
        value = str(tier or "ARCHIVE").strip().upper()
        if value in TIER_ORDER:
            return value
        return ACTION_TO_TIER.get(str(tier or "").strip().lower(), "ARCHIVE")

    def _normalize_action(self, action: Any) -> str:
        value = str(action or "").strip().lower()
        return value if value in ACTION_CHOICES else "save"

    def _downgrade_tier(self, tier: str) -> str:
        if tier not in TIER_ORDER:
            return tier
        idx = max(0, TIER_ORDER.index(tier) - 1)
        return TIER_ORDER[idx]

    def _upgrade_tier(self, tier: str) -> str:
        if tier not in TIER_ORDER:
            return tier
        idx = min(len(TIER_ORDER) - 1, TIER_ORDER.index(tier) + 1)
        return TIER_ORDER[idx]

    def _store_role_metadata(
        self,
        item: Dict[str, Any],
        role_status: dict[str, dict[str, Any]],
        role_payload: Optional[dict[str, Any]],
    ) -> None:
        metadata = item.get("metadata") if isinstance(item.get("metadata"), dict) else {}
        pipeline_metadata = {
            "role_outputs": role_status,
            "role_payload": role_payload or {},
        }
        metadata["role_pipeline"] = pipeline_metadata
        item["metadata"] = metadata
        item["role_outputs"] = role_status

    def _rank_key(self, item: Dict[str, Any]) -> tuple[float, float, float]:
        scores = item.get("scores", {})
        role_tier = self._normalize_tier(item.get("role_pipeline_tier") or item.get("reading_tier"))
        tier_score = TIER_ORDER.index(role_tier) / max(1, len(TIER_ORDER) - 1) if role_tier in TIER_ORDER else 0.0
        return (
            tier_score,
            float(scores.get("personal_score", 0.0) or 0.0),
            float(scores.get("research_relevance", 0.0) or 0.0),
        )

    def _is_repository_item(self, item: Dict[str, Any]) -> bool:
        tier = str(item.get("reading_tier", ""))
        source_type = item.get("source", {}).get("type")
        return bool(
            item.get("is_repository_item")
            or item.get("is_open_source_project")
            or source_type == "github_search"
            or tier in OPEN_SOURCE_ACTIONS
        )

    def _is_benchmark_item(self, item: Dict[str, Any]) -> bool:
        primary = item.get("primary_section", {}) if isinstance(item.get("primary_section"), dict) else {}
        category = item.get("primary_category", {}) if isinstance(item.get("primary_category"), dict) else {}
        return primary.get("id") == "benchmark_evaluation" or category.get("id") == "benchmark_evaluation"

    @property
    def name(self) -> str:
        parts = []
        for role in ROLE_ORDER:
            client = self.clients.get(role)
            if client:
                parts.append(f"{role}:{client.provider}/{client.model}")
        return f"RolePipeline({', '.join(parts)})"
