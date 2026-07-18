from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml
from .base import BaseModel
from .client import ChatModelClient, log_model_error


SUMMARY_FIELDS = [
    "what_is_it",
    "problem",
    "method_or_contribution",
    "why_important",
    "deep_read",
    "suggested_action",
]

ACTION_CHOICES = {
    "read_pdf",
    "skim",
    "watch",
    "save",
    "use_as_eval",
    "clone_and_run",
    "study_code",
    "use_as_baseline",
    "read_readme",
    "archive",
    "ignore",
}

ACTION_CHOICE_TEXT = " / ".join(
    [
        "read_pdf",
        "skim",
        "watch",
        "save",
        "use_as_eval",
        "clone_and_run",
        "study_code",
        "use_as_baseline",
        "read_readme",
        "archive",
        "ignore",
    ]
)

SUMMARY_SYSTEM_PROMPT = (
    "你是严谨的 AI research radar 编辑，面向 George Research Profile v2。"
    "研究画像会随 user payload 提供；必须以该画像为准，不得使用旧的固定四方向。"
    "用自然、具体、克制的中文写摘要，不营销，不编造，不重复套话。"
    "只基于输入信息；信息不足时直接说明需要打开原文确认。"
    "禁止复制或截断英文 abstract；不能编造作者职位、benchmark 或实验结果。"
    "返回严格 JSON，字段必须且只能包含："
    "what_is_it, problem, method_or_contribution, why_important, deep_read, suggested_action。"
    f"suggested_action 只能是 {ACTION_CHOICE_TEXT} 之一。"
)


def load_research_profile(path: str | Path = "config/research_profile.yaml") -> dict[str, Any]:
    profile_path = Path(path)
    if not profile_path.exists():
        return {}
    with open(profile_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


class ProviderSummaryModel(BaseModel):
    """Compatibility wrapper for the old ensemble summarizers."""

    PROVIDER = "unknown"
    DEFAULT_BASE_URL = ""
    DEFAULT_MODEL = ""
    RANK_SCORE_KEY = "personal_score"

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        if not self.base_url:
            self.base_url = self.DEFAULT_BASE_URL
        if not self.model_name:
            self.model_name = self.DEFAULT_MODEL
        self.provider = config.get("provider") or config.get("type") or self.PROVIDER
        self.client = ChatModelClient(
            provider=self.provider,
            api_key=self.api_key or "",
            base_url=self.base_url or "",
            model=self.model_name or "",
        )

    def summarize(self, item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if not self.api_key:
            return None

        parsed = self.client.call_json(
            system_prompt=SUMMARY_SYSTEM_PROMPT,
            user_payload=self._build_prompt(item),
            temperature=0.2,
        )
        if parsed is None:
            return None
        return self._validate_response(parsed)

    def rank(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return sorted(items, key=lambda x: x.get("scores", {}).get(self.RANK_SCORE_KEY, 0), reverse=True)

    def _build_prompt(self, item: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "title": item.get("title"),
            "source": item.get("source", {}),
            "url": item.get("url"),
            "abstract_or_excerpt": (item.get("abstract") or item.get("summary") or "")[:2200],
            "metadata": item.get("metadata", {}),
            "primary_section": item.get("primary_section", {}),
            "primary_category": item.get("primary_category", {}),
            "secondary_tags": item.get("secondary_tags", []),
            "matched_sections": item.get("matched_sections", []),
            "reading_tier": item.get("reading_tier"),
            "matched_focus_areas": item.get("matched_focus_areas", []),
            "matched_keywords": item.get("matched_keywords", []),
            "research_profile": load_research_profile(),
            "track_relevance": item.get("track_relevance", {}),
            "project_relevance": item.get("project_relevance", {}),
            "scores": item.get("scores", {}),
            "is_open_source_project": item.get("is_open_source_project", False),
            "required_fields": {
                "what_is_it": "这是什么？",
                "problem": "解决了什么问题？",
                "method_or_contribution": "方法或贡献是什么？",
                "why_important": "为什么对 George 重要？",
                "deep_read": "是否建议深读？",
                "suggested_action": f"建议行动，只能是 {ACTION_CHOICE_TEXT} 之一",
            },
        }

    def _validate_response(self, parsed: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if not all(key in parsed for key in SUMMARY_FIELDS):
            log_model_error(
                self.provider,
                self.model_name or "",
                self.base_url or "",
                "n/a",
                "Response JSON did not include all required summary fields.",
            )
            return None

        result = {field: parsed.get(field, "") for field in SUMMARY_FIELDS}
        action = str(result.get("suggested_action") or "").strip().lower()
        result["suggested_action"] = action if action in ACTION_CHOICES else "save"
        return result
