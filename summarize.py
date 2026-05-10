from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import requests
import yaml
from jinja2 import Environment, FileSystemLoader

from md_to_html import archive_report_with_timestamp, generate_html_report

LLM_SUMMARY_CALLS = 0


KIND_LABELS = {
    "primary": "一手来源",
    "aggregator": "聚合/摘要",
    "media": "媒体摘要",
}

GROUP_LABELS = {
    "core_focus": "重点研究方向",
    "primary_research": "重点研究方向",
    "traditional_ai": "传统 AI 基础领域",
    "traditional_fields": "传统 AI 基础领域",
    "other": "Other Highlights",
}

TIER_LABELS = {
    "MUST_READ": "MUST_READ",
    "SKIM": "SKIM",
    "WATCH": "WATCH",
    "ARCHIVE": "ARCHIVE",
    "IGNORE": "IGNORE",
    "clone_and_run": "clone_and_run",
    "study_code": "study_code",
    "use_as_baseline": "use_as_baseline",
    "read_readme": "read_readme",
    "save": "save",
    "archive": "archive",
}

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
    "ignore",
    "use_as_eval",
    "clone_and_run",
    "study_code",
    "use_as_baseline",
    "read_readme",
    "archive",
}

OPEN_SOURCE_ACTIONS = {"study_code", "use_as_baseline", "clone_and_run", "read_readme", "save", "archive"}

DEFAULT_TEMPLATE_PATH = Path("config") / "daily_report.md.j2"
LLM_SUMMARY_CALLS = 0

SECTION_DISPLAY_NAMES = {
    "context_compression_memory": "上下文压缩 / 长上下文 / 记忆",
    "context_compression": "上下文压缩 / 长上下文 / 记忆",
    "context_memory": "上下文压缩 / 长上下文 / 记忆",
    "agents": "Agent / Reasoning / Inference-time Scaling / Planning",
    "open_world_learning": "新类学习 / 开放世界学习",
    "open_world": "新类学习 / 开放世界学习",
    "model_distillation": "模型蒸馏 / 模型压缩",
    "distillation_efficiency": "模型蒸馏 / 模型压缩",
    "cv": "CV",
    "nlp": "NLP",
    "rl": "RL",
    "model_architecture": "模型架构",
    "architecture": "模型架构",
    "learning_methods": "学习方法",
    "highlights": "其他方向最耀眼成果",
    "other_highlights": "其他方向最耀眼成果",
    "benchmark_evaluation": "Benchmark / Dataset / Evaluation",
    "github_projects": "GitHub / 开源项目推荐",
    "institutional_updates": "企业 / 大学 / 研究所动态",
}


def load_json(path: str | Path) -> Any:
    with open(path, "r", encoding="utf-8-sig") as f:
        return json.load(f)


def trim(text: str, limit: int = 360) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def openai_enabled() -> bool:
    return bool(os.getenv("OPENAI_API_KEY"))


def ensemble_enabled() -> bool:
    return os.getenv("MODEL_MODE") == "ensemble"


def _replace_env_var(value: str) -> str:
    """替换字符串中的环境变量引用 ${VAR_NAME}"""
    if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
        env_var = value[2:-1]
        return os.getenv(env_var, value)
    return value


def load_model_config() -> dict[str, Any]:
    config_path = Path("config") / "models.yaml"
    if not config_path.exists():
        return {}
    
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    for model in config.get("models", []):
        for key in ["api_key", "base_url", "model"]:
            if key in model:
                model[key] = _replace_env_var(model[key])
    
    editor_config = config.get("editor", {})
    for key in ["api_key", "base_url", "model"]:
        if key in editor_config:
            editor_config[key] = _replace_env_var(editor_config[key])
    
    return config


def get_ensemble_model():
    try:
        from models.ensemble import EnsembleModel
        config = load_model_config()
        return EnsembleModel(config)
    except ImportError:
        return None


def openai_timeout_seconds() -> float:
    return float(os.getenv("OPENAI_TIMEOUT_SECONDS", "20"))


def openai_summary_budget() -> int:
    return int(os.getenv("OPENAI_SUMMARY_BUDGET", "12"))


GROUNDING_LABELS = {
    "title_only": "title only",
    "abstract_only": "abstract only",
    "full_text": "full text",
    "repo_readme": "repo README",
}


def metadata_dict(item: dict[str, Any]) -> dict[str, Any]:
    metadata = item.get("metadata")
    return metadata if isinstance(metadata, dict) else {}


def repo_readme_summary(item: dict[str, Any]) -> str:
    metadata = metadata_dict(item)
    for key in ["repo_readme_summary", "readme_summary", "readme_excerpt"]:
        value = metadata.get(key)
        if value:
            return str(value)
    return ""


def is_repository_item(item: dict[str, Any]) -> bool:
    tier = str(item.get("reading_tier", ""))
    source_type = item.get("source", {}).get("type")
    return bool(item.get("is_repository_item") or item.get("is_open_source_project") or source_type == "github_search" or tier in {"clone_and_run", "study_code", "use_as_baseline", "read_readme", "save", "archive"})


def grounding_level(item: dict[str, Any]) -> str:
    existing = str(item.get("grounding_level") or "").strip()
    if existing in GROUNDING_LABELS:
        return existing
    if is_repository_item(item):
        return "repo_readme" if repo_readme_summary(item) else "title_only"
    summary = str(item.get("abstract") or item.get("summary") or "").strip()
    if not summary:
        return "title_only"
    source_type = str(item.get("source", {}).get("type", "")).lower()
    if source_type in {"arxiv", "openreview", "hf_daily_papers", "hf_papers_page"}:
        return "abstract_only"
    return "full_text"


def grounding_label(item: dict[str, Any]) -> str:
    return GROUNDING_LABELS.get(grounding_level(item), "abstract only")


def allowed_evidence_text(item: dict[str, Any]) -> str:
    pieces = [
        str(item.get("title", "")),
        str(item.get("abstract") or item.get("summary") or ""),
        json.dumps(item.get("source", {}), ensure_ascii=False),
        str(item.get("url", "")),
        json.dumps(metadata_dict(item), ensure_ascii=False),
        repo_readme_summary(item),
    ]
    return "\n".join(piece for piece in pieces if piece.strip())


def is_benchmark_item(item: dict[str, Any]) -> bool:
    return item.get("primary_section", {}).get("id") == "benchmark_evaluation" or item.get("primary_category", {}).get("id") == "benchmark_evaluation"


def benchmark_action(item: dict[str, Any]) -> str:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    if any(term in text for term in ["agent", "workflow", "planning", "long-horizon", "long horizon", "memory", "safety"]):
        return "use_as_eval"
    if any(term in text for term in ["medical", "epidemic", "video", "domain generalization"]):
        return "save"
    if any(term in text for term in ["benchmark", "dataset", "evaluation"]):
        return "skim"
    return "ignore"


def apply_action_constraints(action: str, item: dict[str, Any]) -> str:
    """
    应用 suggested_action 的硬约束：
    
    1. 如果 reading_tier 是 WATCH 或 ARCHIVE，则 suggested_action 不得为 read_pdf
    2. 如果 reading_tier 是 SKIM，则 suggested_action 不得为 read_pdf（除非 explicit_override=true）
    3. 如果 is_open_source_project=true，则 suggested_action 只能是：
       study_code / use_as_baseline / clone_and_run / read_readme / save / archive
    4. 如果 grounding_level=title_only，则 suggested_action 不得为 read_pdf
    5. 如果 primary_category 是 GitHub / Open Source Projects，则不得进入今日深读清单
    """
    tier = item.get("reading_tier", "").upper()
    is_open_source = item.get("is_open_source_project", False)
    ground_level = grounding_level(item)
    explicit_override = item.get("explicit_override", False)
    
    if action == "read_pdf":
        if tier in {"WATCH", "ARCHIVE"}:
            return "watch" if tier == "WATCH" else "save"
        if tier == "SKIM" and not explicit_override:
            return "skim"
        if is_open_source:
            return "read_readme"
        if ground_level == "title_only":
            return "save"
        
        section_title = item.get("primary_category", {}).get("title", "")
        if section_title == "GitHub / Open Source Projects":
            return "read_readme"
    
    if is_open_source and action not in OPEN_SOURCE_ACTIONS:
        return "read_readme"
    
    return action


def choose_action(item: dict[str, Any]) -> str:
    tier = item.get("reading_tier", "ARCHIVE")
    scores = item.get("scores", {})
    if is_repository_item(item):
        action = item.get("github_action") or tier if tier in ACTION_CHOICES else "read_readme"
        return apply_action_constraints(action, item)
    if is_benchmark_item(item):
        action = item.get("benchmark_action") or benchmark_action(item)
        return apply_action_constraints(action, item)
    if tier == "IGNORE":
        return "ignore"
    if tier == "MUST_READ":
        return apply_action_constraints("read_pdf", item)
    if tier == "SKIM":
        return apply_action_constraints("skim", item)
    if tier == "WATCH":
        return apply_action_constraints("watch", item)
    return apply_action_constraints("save", item)


def normalize_action(value: Any, item: dict[str, Any]) -> str:
    action = str(value or "").strip().lower()
    if action in ACTION_CHOICES:
        return apply_action_constraints(action, item)
    return choose_action(item)


def normalize_summary(payload: dict[str, Any] | None, item: dict[str, Any]) -> dict[str, str]:
    fallback = fallback_summary(item)
    if not isinstance(payload, dict):
        return fallback

    normalized: dict[str, str] = {}
    for field in SUMMARY_FIELDS:
        value = str(payload.get(field, "")).strip()
        normalized[field] = value or fallback[field]
    normalized["suggested_action"] = normalize_action(normalized["suggested_action"], item)
    return normalized


def salient_terms(item: dict[str, Any], limit: int = 5) -> list[str]:
    terms: list[str] = []
    for term in item.get("matched_keywords", []):
        text = str(term).strip()
        if text and text.lower() not in {"benchmark", "dataset", "evaluation", "paper", "method"}:
            terms.append(text)
    evidence = f"{item.get('title', '')} {item.get('summary', '')}"
    for token in re.findall(r"\b[A-Z][A-Za-z0-9]*(?:[-_][A-Za-z0-9]+)*\b", evidence):
        if len(token) >= 3 and token not in terms:
            terms.append(token)
    return terms[:limit]


def item_kind_cn(item: dict[str, Any]) -> str:
    if is_repository_item(item):
        return "开源项目"
    if is_benchmark_item(item):
        return "评测基准或数据集论文"
    source_type = str(item.get("source", {}).get("type", "")).lower()
    if source_type in {"arxiv", "openreview", "hf_daily_papers", "hf_papers_page"}:
        return "研究论文"
    return "研究动态"


def contribution_hint_cn(item: dict[str, Any], names: list[str]) -> str:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    name_text = "、".join(names[:4])
    if is_repository_item(item):
        return "这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。"
    if any(word in text for word in ["introduce", "introduces", "present", "presents", "propose", "proposes"]):
        if name_text:
            return f"摘要可确认它提出或引入了 {name_text}；具体训练设置、指标和消融细节需读原文确认。"
        return "摘要可确认它提出了新的方法、数据或评测设定；方法细节未在摘要中充分展开。"
    if any(word in text for word in ["benchmark", "dataset", "evaluation", "evaluate"]):
        return "摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。"
    return "方法细节未在摘要中充分展开，细节需读原文确认。"


def fallback_summary(item: dict[str, Any]) -> dict[str, Any]:
    section = item.get("primary_category", item.get("primary_section", {})).get("title", "相关方向")
    tier = item.get("reading_tier", "ARCHIVE")
    scores = item.get("scores", {})
    names = salient_terms(item)
    keywords = "、".join(names[:4])
    title = item.get("title") or "未命名条目"

    if grounding_level(item) == "title_only":
        what_is_it = f"从标题可判断，这是关于“{title}”的{item_kind_cn(item)}，目前缺少摘要支撑。"
    else:
        focus = f"，核心信号包括 {keywords}" if keywords else ""
        what_is_it = f"这是一篇/项归入“{section}”的{item_kind_cn(item)}{focus}。"

    if keywords:
        problem = f"它关注“{section}”里的 {keywords} 等问题。"
    else:
        problem = f"它与“{section}”相关，但摘要中的问题表述不够具体。"

    method_or_contribution = contribution_hint_cn(item, names)

    importance_parts = [f"tier={tier}", f"editorial_priority={item.get('editorial_priority', 0):.2f}"]
    if tier == "MUST_READ":
        importance_parts.append("今天安排深读。")
    elif tier == "SKIM":
        importance_parts.append("今天快速扫读。")
    elif tier == "WATCH":
        importance_parts.append("方向相关，先追踪不深读。")
    elif tier == "ARCHIVE":
        importance_parts.append("归档备用。")
    elif tier in ACTION_CHOICES:
        importance_parts.append("按 GitHub 项目动作处理。")
    else:
        importance_parts.append("不进入正文阅读队列。")

    importance_parts.append(f"personal={scores.get('personal_score', 0):.2f}，relevance={scores.get('research_relevance', 0):.2f}。")

    action = choose_action(item)
    deep_read = "建议今天深读。" if action == "read_pdf" else "今天不深读，先按行动建议处理。"
    if tier == "IGNORE":
        deep_read = "不建议深读。"

    return {
        "what_is_it": what_is_it,
        "problem": problem,
        "method_or_contribution": method_or_contribution,
        "why_important": " ".join(importance_parts),
        "deep_read": deep_read,
        "suggested_action": action,
    }


def summarize_with_openai(item: dict[str, Any]) -> dict[str, Any] | None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.getenv("OPENAI_MODEL") or "gpt-4o-mini"
    if grounding_level(item) == "title_only":
        return None
    evidence = trim(allowed_evidence_text(item), 2600)
    prompt = {
        "title": item.get("title"),
        "source": item.get("source", {}),
        "url": item.get("url"),
        "metadata": metadata_dict(item),
        "repo_readme_summary": repo_readme_summary(item),
        "allowed_evidence": evidence,
        "grounding_level": grounding_level(item),
        "primary_section": item.get("primary_section", {}),
        "secondary_tags": item.get("secondary_tags", []),
        "reading_tier": item.get("reading_tier"),
        "matched_focus_areas": item.get("matched_focus_areas", []),
        "matched_keywords": item.get("matched_keywords", []),
        "scores": item.get("scores", {}),
        "is_open_source_project": item.get("is_open_source_project", False),
        "required_fields": {
            "what_is_it": "这是什么？",
            "problem": "解决了什么问题？",
            "method_or_contribution": "方法或贡献是什么？",
            "why_important": "为什么对我重要？",
            "deep_read": "是否建议深读？",
            "suggested_action": "建议行动，只能是 read_pdf / skim / watch / save / use_as_eval / clone_and_run / study_code / use_as_baseline / read_readme / archive / ignore 之一",
        },
    }
    messages = [
        {
            "role": "system",
            "content": (
                "你是严谨的 AI research radar 编辑，面向一位关注长上下文、Agent、开放世界学习和模型压缩的研究者。"
                "用自然、具体、克制的中文写摘要，不营销，不编造，不重复套话。"
                "grounding 不是禁止总结，而是禁止编造：允许基于 title、abstract、full text 或 README 做忠实中文归纳。"
                "禁止复制或截断英文 abstract；即使 grounding_level 是 abstract_only，也必须用中文概括。"
                "只基于 allowed_evidence 中真实出现的信息；信息不足时直接说明“方法细节未在摘要中充分展开”，最多在末尾补一句“细节需读原文确认”。"
                "如果写出具体数字、模型名、数据集名或 benchmark 结果，它必须能在 allowed_evidence 中逐字找到。"
                "grounding_level 为 title_only 或 abstract_only 时，不得扩展实验结论、系统细节或未给出的因果解释。"
                "避免模板化表达，不要按来源类型写泛泛的跟踪价值判断。"
                "不要反复使用空泛的免责句；只在确实缺信息时简短提示。"
                "返回严格 JSON，字段必须且只能包含："
                "what_is_it, problem, method_or_contribution, why_important, deep_read, suggested_action。"
                "suggested_action 只能是 read_pdf、skim、watch、save、use_as_eval、clone_and_run、study_code、use_as_baseline、read_readme、archive、ignore 之一。"
                "每个字段 1-2 句，尽量指出具体方法名、任务、数据、系统或实验线索。"
            ),
        },
        {"role": "user", "content": json.dumps(prompt, ensure_ascii=False)},
    ]
    try:
        response = requests.post(
            f"{base_url}/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": model,
                "messages": messages,
                "temperature": 0.2,
                "response_format": {"type": "json_object"},
            },
            timeout=openai_timeout_seconds(),
        )
        response.raise_for_status()
        parsed = json.loads(response.json()["choices"][0]["message"]["content"])
        if all(key in parsed for key in SUMMARY_FIELDS):
            return normalize_summary(parsed, item)
    except Exception:
        return None
    return None


def summarize_item(item: dict[str, Any]) -> dict[str, Any]:
    global LLM_SUMMARY_CALLS
    
    if ensemble_enabled():
        ensemble_model = get_ensemble_model()
        if ensemble_model:
            try:
                result = ensemble_model.summarize(item)
                if result:
                    return normalize_summary(result, item)
            except Exception as e:
                print(f"Ensemble model error: {e}")
    
    if openai_enabled() and LLM_SUMMARY_CALLS < openai_summary_budget():
        LLM_SUMMARY_CALLS += 1
        return normalize_summary(summarize_with_openai(item), item)
    
    return fallback_summary(item)


def score_line(item: dict[str, Any]) -> str:
    scores = item.get("scores", {})
    return (
        f"global_score {scores.get('global_score', 0):.2f}；"
        f"personal_score {scores.get('personal_score', 0):.2f}；"
        f"novelty {scores.get('novelty', 0):.2f}；"
        f"credibility {scores.get('credibility', 0):.2f}；"
        f"evidence_strength {scores.get('evidence_strength', 0):.2f}；"
        f"community_signal {scores.get('community_signal', 0):.2f}；"
        f"actionability {scores.get('actionability', 0):.2f}；"
        f"research_relevance {scores.get('research_relevance', 0):.2f}"
    )


def item_block(item: dict[str, Any], idx: int) -> str:
    source = item.get("source", {})
    kind = source.get("kind", "primary")
    published = item.get("published_at") or "未知"
    keywords = "、".join(item.get("matched_keywords", [])[:10]) or "无明显关键词"
    primary = item.get("primary_category") or item.get("primary_section", {})
    focus = section_display_name(primary.get("id", ""), primary.get("title", "未分类"))
    secondary_tags = "、".join(str(tag.get("title") or tag.get("id")) for tag in item.get("secondary_tags", [])[:8] if isinstance(tag, dict)) or "无"
    duplicate_names = sorted({s.get("name", "") for s in item.get("duplicate_sources", []) if s.get("name")})
    duplicate_text = "、".join(duplicate_names[:5]) if len(duplicate_names) > 1 else ""
    summary = summarize_item(item)
    tier_caption = "行动标签" if is_repository_item(item) else "阅读层级"

    lines = [
        f"##### {idx}. [{item.get('title')}]({item.get('url')})",
        f"- {tier_caption}：{TIER_LABELS.get(item.get('reading_tier'), item.get('reading_tier', 'ARCHIVE'))}",
        f"- 来源：{source.get('name', '未知')}",
        f"- 来源类型：{KIND_LABELS.get(kind, kind)}",
        f"- 证据来源：{grounding_label(item)}",
        f"- 原文链接：{item.get('url')}",
        f"- 发布时间：{published}",
        f"- 这是什么？{summary.get('what_is_it', '').strip()}",
        f"- 解决了什么问题？{summary.get('problem', '').strip()}",
        f"- 方法或贡献是什么？{summary.get('method_or_contribution', '').strip()}",
        f"- 为什么对我重要？{summary.get('why_important', '').strip()}",
        f"- 是否建议深读？{summary.get('deep_read', '').strip()}",
        f"- 建议行动：{summary.get('suggested_action', choose_action(item)).strip()}",
        f"- 评分：{score_line(item)}",
        f"- 命中方向：{focus}",
        f"- 相关标签：{secondary_tags}",
        f"- 命中关键词：{keywords}",
    ]
    if item.get("is_open_source_project"):
        metadata = item.get("metadata", {})
        metrics = item.get("metrics", {})
        if metrics.get("stars") is not None:
            stars = metrics.get("stars", 0)
            forks = metrics.get("forks", 0)
            license_info = metadata.get("license", "") or "未知"
            has_examples = "✅" if metadata.get("has_examples") else "❌"
            has_docs = "✅" if metadata.get("has_docs") else "❌"
            paper_link = metadata.get("paper_link", "")
            readme_summary = metadata.get("repo_readme_summary", "") or metadata.get("readme_excerpt", "")[:300]
            
            lines.append(f"- 开源信号：⭐ {stars} | 🍴 {forks} | 📜 {license_info}")
            lines.append(f"- 示例/文档：示例 {has_examples} | 文档 {has_docs}")
            if paper_link:
                lines.append(f"- 关联论文：{paper_link}")
            if readme_summary:
                lines.append(f"- README 摘要：{readme_summary[:300]}")
        else:
            lines.append("- 开源信号：标题、摘要或来源中出现代码/开源线索。")
    if item.get("link_quality") == "low":
        lines.insert(5, "- link_quality: low")
    if duplicate_text:
        lines.append(f"- 去重信息：同一内容也出现在 {duplicate_text}")
    return "\n".join(lines)


def compact_item(item: dict[str, Any]) -> str:
    section = item.get("primary_section", {}).get("title", "未分类")
    scores = item.get("scores", {})
    tier = item.get("reading_tier", "ARCHIVE")
    return (
        f"- [{item.get('title')}]({item.get('url')})"
        f"（{tier}，{section}，证据 {grounding_label(item)}，personal {scores.get('personal_score', 0):.2f}，global {scores.get('global_score', 0):.2f}）"
    )


def grouped_sections(
    processed: dict[str, Any],
    group: str | set[str],
    *,
    exclude_ids: set[str] | None = None,
) -> list[dict[str, Any]]:
    groups = {group} if isinstance(group, str) else group
    exclude_ids = exclude_ids or set()
    return [
        section
        for section in processed.get("sections", [])
        if section.get("group") in groups and section.get("id") not in exclude_ids
    ]


def score_rank(item: dict[str, Any]) -> tuple[float, float, float]:
    scores = item.get("scores", {})
    return (
        scores.get("personal_score", 0),
        scores.get("global_score", 0),
        scores.get("research_relevance", 0),
    )


def render_archive_titles(items: list[dict[str, Any]], limit: int = 8, label: str = "归档候选") -> list[str]:
    if not items:
        return []
    lines = ["", f"{label}："]
    for item in sorted(items, key=score_rank, reverse=True)[:limit]:
        lines.append(compact_item(item))
    return lines


def render_research_group(title: str, sections: list[dict[str, Any]]) -> list[str]:
    lines = [f"## {title}"]
    single_same_title = len(sections) == 1 and sections[0].get("title") == title
    for section in sections:
        group = section.get("group")
        section_id = section.get("id")
        items = sorted(
            [item for item in section.get("items", []) if item.get("reading_tier") != "IGNORE"],
            key=score_rank,
            reverse=True,
        )
        must_items = [item for item in items if item.get("reading_tier") == "MUST_READ"]
        skim_items = [item for item in items if item.get("reading_tier") == "SKIM"]
        watch_items = [item for item in items if item.get("reading_tier") == "WATCH"]
        archive_items = [item for item in items if item.get("reading_tier") == "ARCHIVE"]

        lines.append("")
        if not single_same_title:
            lines.append(f"### {section.get('title')}")

        if group in {"core_focus", "primary_research"}:
            body_items = must_items[:1] + skim_items[:2]
            if body_items:
                for idx, item in enumerate(body_items, 1):
                    lines.append(item_block(item, idx))
                    lines.append("")
            else:
                lines.append("- 今日没有 MUST_READ / SKIM 条目。")
            lines.extend(render_archive_titles(watch_items, limit=6, label="WATCH 跟踪"))
            lines.extend(render_archive_titles(archive_items))
            continue

        if group in {"traditional_ai", "traditional_fields"}:
            shown_items = (must_items + skim_items + watch_items + archive_items)[:2]
        elif group == "other" or section_id == "highlights":
            shown_items = (must_items + skim_items + watch_items + archive_items)[:5]
        else:
            shown_items = must_items + skim_items + watch_items + archive_items

        if shown_items:
            for idx, item in enumerate(shown_items, 1):
                lines.append(item_block(item, idx))
                lines.append("")
        else:
            lines.append("- 今日没有 MUST_READ / SKIM 条目。")
    lines.append("")
    return lines


def unique_section_items(sections: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_key: dict[str, dict[str, Any]] = {}
    for section in sections:
        for item in section.get("items", []):
            if item.get("reading_tier") == "IGNORE":
                continue
            key = item.get("id") or item.get("url") or item.get("title")
            existing = by_key.get(key)
            if not existing or score_rank(item) > score_rank(existing):
                by_key[key] = item
    return sorted(by_key.values(), key=score_rank, reverse=True)


def render_other_highlights(sections: list[dict[str, Any]]) -> list[str]:
    lines = ["## Other Highlights"]
    items = unique_section_items(sections)[:5]
    if not items:
        lines.append("- 今日没有进入正文的 Other Highlights。")
        lines.append("")
        return lines
    for idx, item in enumerate(items, 1):
        lines.append(item_block(item, idx))
        lines.append("")
    return lines


def render_github_projects(projects: list[dict[str, Any]]) -> list[str]:
    lines = ["## GitHub / Open-source Projects"]
    if not projects:
        lines.append("- 今日没有进入正文的开源项目候选。")
        lines.append("")
        return lines

    for idx, item in enumerate(projects[:5], 1):
        lines.append(item_block(item, idx))
        lines.append("")
    return lines


def render_classics(classics: list[dict[str, Any]]) -> list[str]:
    lines = ["## 温故而知新 / Classic Paper Revisit"]
    if not classics:
        lines.append("- 今日没有足够明确的主题连接，暂不推荐经典论文。")
        lines.append("")
        return lines

    for idx, paper in enumerate(classics, 1):
        related_sections = "、".join(paper.get("related_sections", [])) or "相关方向"
        authors = "、".join(str(author) for author in paper.get("authors", [])[:8])
        if len(paper.get("authors", [])) > 8:
            authors += " 等"
        topic_tags = "、".join(str(tag) for tag in paper.get("topic_tags", [])[:8])
        lines.extend(
            [
                f"### {idx}. [{paper.get('title')}]({paper.get('url')})（{paper.get('year')}）",
                f"- 作者：{authors or '未知'}",
                f"- topic_tags：{topic_tags or '未标注'}",
                f"- 关联方向：{related_sections}",
                f"- 为什么经典：{paper.get('why_classic') or paper.get('why_now')}",
            ]
        )
        concept = paper.get("concept_connection") or {}
        if concept:
            lines.append(f"- 今日新论文继承了什么问题：{concept.get('inherits', '需要打开今日论文确认。')}")
            lines.append(f"- 它挑战了什么经典假设：{concept.get('challenges', '需要打开今日论文确认。')}")
            lines.append(f"- 它推进到什么新场景：{concept.get('extends', '需要打开今日论文确认。')}")
        else:
            lines.append(f"- 它和今日新论文的概念连接：{paper.get('modern_connection', '今天没有足够明确的新论文连接；作为基础脉络复习。')}")
        if paper.get("prerequisite"):
            lines.append(f"- 预备知识：{paper.get('prerequisite')}")
        related_today = paper.get("related_today", [])
        if related_today:
            lines.append("- 相关今日条目：")
            for item in related_today:
                terms = "、".join(item.get("connection_terms", []))
                suffix = f"；连接词：{terms}" if terms else ""
                lines.append(f"  - [{item.get('title')}]({item.get('url')})（{item.get('section')}{suffix}）")
        lines.append("")
    return lines


def section_display_name(section_id: str, fallback: str | None = None) -> str:
    return SECTION_DISPLAY_NAMES.get(section_id, fallback or section_id)


def get_section(processed: dict[str, Any], section_id: str) -> dict[str, Any]:
    for section in processed.get("sections", []):
        if section.get("id") == section_id:
            return section
    return {"id": section_id, "title": section_display_name(section_id), "items": []}


def items_for_section(processed: dict[str, Any], section_ids: list[str]) -> list[dict[str, Any]]:
    by_key: dict[str, dict[str, Any]] = {}
    for section_id in section_ids:
        for item in get_section(processed, section_id).get("items", []):
            if item.get("reading_tier") == "IGNORE":
                continue
            key = item.get("id") or item.get("url") or item.get("title")
            existing = by_key.get(key)
            if not existing or score_rank(item) > score_rank(existing):
                by_key[key] = item
    return sorted(by_key.values(), key=score_rank, reverse=True)


def items_by_tier(items: list[dict[str, Any]], tier: str) -> list[dict[str, Any]]:
    return [item for item in items if item.get("reading_tier") == tier]


def render_full_items(items: list[dict[str, Any]], *, limit: int = 3, empty: str = "- 无。") -> str:
    if not items:
        return empty
    blocks = [item_block(item, idx) for idx, item in enumerate(items[:limit], 1)]
    return "\n\n".join(blocks)


def render_compact_items(items: list[dict[str, Any]], *, limit: int = 6, empty: str = "- 无。") -> str:
    if not items:
        return empty
    return "\n".join(compact_item(item) for item in items[:limit])


def render_primary_section(processed: dict[str, Any], section_ids: list[str]) -> dict[str, str]:
    items = items_for_section(processed, section_ids)
    return {
        "must_read": render_full_items(items_by_tier(items, "MUST_READ"), limit=1),
        "skim": render_full_items(items_by_tier(items, "SKIM"), limit=2),
        "watch": render_compact_items(items_by_tier(items, "WATCH"), limit=3),
        "archive": render_compact_items(items_by_tier(items, "ARCHIVE"), limit=8),
    }


def render_traditional_section(processed: dict[str, Any], section_id: str) -> str:
    items = items_for_section(processed, [section_id])
    shown = items_by_tier(items, "MUST_READ") + items_by_tier(items, "SKIM") + items_by_tier(items, "WATCH") + items_by_tier(items, "ARCHIVE")
    return render_compact_items(shown, limit=2, empty="- 今日无明显条目。")


def has_official_or_multi_source_signal(item: dict[str, Any]) -> bool:
    source = item.get("source", {})
    text = " ".join(
        [
            str(source.get("id", "")),
            str(source.get("name", "")),
            str(source.get("url", "")),
            str(item.get("url", "")),
        ]
    ).lower()
    official = any(
        token in text
        for token in [
            "openai",
            "anthropic",
            "deepmind",
            "google",
            "meta",
            "microsoft",
            "nvidia",
            "apple",
            "stanford",
            "mit",
            "berkeley",
            "neurips",
            "icml",
            "iclr",
            "thecvf",
        ]
    )
    return official or len(item.get("duplicate_sources", []) or []) > 1 or item.get("is_open_source_project")


def is_strict_other_highlight(item: dict[str, Any]) -> bool:
    scores = item.get("scores", {})
    source_type = str(item.get("source", {}).get("type", "")).lower()
    plain_arxiv = source_type in {"arxiv", "hf_daily_papers", "hf_papers_page"}
    strong_signal = (
        has_official_or_multi_source_signal(item)
        or scores.get("community_signal", 0) >= 0.25
        or scores.get("actionability", 0) >= 0.72
    )
    if plain_arxiv and not strong_signal:
        return False
    return (
        scores.get("global_score", 0) >= 0.78
        and scores.get("credibility", 0) >= 0.75
        and scores.get("evidence_strength", 0) >= 0.65
        and strong_signal
    )


def render_other_section(processed: dict[str, Any], section_ids: list[str], *, limit: int = 5) -> str:
    items = items_for_section(processed, section_ids)
    if any(section_id in {"highlights", "other_highlights"} for section_id in section_ids):
        strict = [
            item
            for item in items
            if item.get("reading_tier") in {"MUST_READ", "SKIM", "WATCH"} and is_strict_other_highlight(item)
        ]
        other_watch = [
            item
            for item in items
            if item not in strict and item.get("reading_tier") in {"WATCH", "ARCHIVE"}
        ]
        lines = [render_full_items(strict, limit=limit, empty="- 今日没有达到高影响阈值的 Other Highlights。")]
        if other_watch:
            lines.append("")
            lines.append("Other Watch / Archive：")
            lines.append(render_compact_items(other_watch, limit=8))
        return "\n".join(lines)
    shown = items_by_tier(items, "MUST_READ") + items_by_tier(items, "SKIM") + items_by_tier(items, "WATCH") + items_by_tier(items, "ARCHIVE")
    return render_full_items(shown, limit=limit, empty="- 今日无明显条目。")


def benchmark_ability(item: dict[str, Any]) -> str:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    if "workflow fidelity" in text or "payment" in text:
        return "评估 LLM agent 在真实/拟真 workflow 中是否按预期完成轨迹与关键步骤。"
    if "video action" in text or "viddiff" in text:
        return "评估多模态模型区分同一动作视频之间细粒度语义差异的能力。"
    if "spatialepi" in text or "epidemic" in text:
        return "评估时空流行病预测中空间信息、流行病先验和滚动预测协议的有效性。"
    if "medarabench" in text or "arabic medical" in text:
        return "评估阿拉伯语医学多项选择问答与多语言医学能力。"
    if "agent" in text or "planning" in text:
        return "评估 agent 规划、执行或环境交互能力。"
    if "dataset" in text or "benchmark" in text or "evaluation" in text:
        return "评估摘要中描述的任务能力；具体指标需打开原文确认。"
    return "标题信号不足，需打开原文确认评估对象。"


def benchmark_fit(item: dict[str, Any]) -> str:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    if "workflow fidelity" in text or "payment" in text:
        return "适合用于 agent evaluation、long-horizon workflow、轨迹保真度和安全执行研究。"
    if "video action" in text or "viddiff" in text:
        return "适合用于 VLM/视频理解中的细粒度动作差异评测，不是当前四条主线的核心实验。"
    if "spatialepi" in text or "epidemic" in text:
        return "适合用于 AI for science、时空预测和科学 benchmark 设计参考。"
    if "medarabench" in text or "arabic medical" in text:
        return "适合用于多语言医学 QA、低资源语言评测和领域安全性测试。"
    if any(term in text for term in ["agent", "planning", "memory", "long context", "safety"]):
        return "适合用于 agent evaluation / memory / long-horizon planning 相关实验。"
    if any(term in text for term in ["domain generalization", "multimodal"]):
        return "适合用于多模态泛化或跨域评测设计参考。"
    return "适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。"


def benchmark_baseline_use(item: dict[str, Any]) -> str:
    action = benchmark_action(item)
    if action == "use_as_eval":
        return "可以优先评估是否作为实验基准。"
    if action in {"skim", "save"}:
        return "暂不作为核心基准，先保存评测协议和指标设计。"
    return "不建议作为当前实验基准。"


def benchmark_layer(item: dict[str, Any]) -> str:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    scores = item.get("scores", {})
    core_terms = [
        "agent",
        "workflow",
        "planning",
        "long-horizon",
        "long horizon",
        "memory",
        "safety",
        "ood",
        "open-world",
        "distillation",
        "compression",
    ]
    if any(term in text for term in core_terms) and (
        scores.get("personal_score", 0) >= 0.62 or scores.get("research_relevance", 0) >= 0.65
    ):
        return "core"
    if scores.get("global_score", 0) >= 0.62 or scores.get("actionability", 0) >= 0.55:
        return "interesting"
    return "other"


def benchmark_block(item: dict[str, Any], idx: int) -> str:
    source = item.get("source", {})
    tier = item.get("reading_tier", "ARCHIVE")
    action = benchmark_action(item)
    return "\n".join(
        [
            f"##### {idx}. [{item.get('title')}]({item.get('url')})",
            f"- 阅读层级：{tier}",
            f"- 来源：{source.get('name', '未知')}",
            f"- 证据来源：{grounding_label(item)}",
            f"- benchmark 评估什么能力：{benchmark_ability(item)}",
            f"- 适合用于什么研究：{benchmark_fit(item)}",
            f"- 可否作为实验基准：{benchmark_baseline_use(item)}",
            f"- 建议行动：{action}",
        ]
    )


def benchmark_items(processed: dict[str, Any]) -> list[dict[str, Any]]:
    items = items_for_section(processed, ["benchmark_evaluation"])
    shown = items_by_tier(items, "MUST_READ") + items_by_tier(items, "SKIM") + items_by_tier(items, "WATCH") + items_by_tier(items, "ARCHIVE")
    return shown


def benchmark_appendix_path(report_date: str) -> Path:
    return Path("reports") / "appendix" / f"{report_date}-benchmarks.md"


def write_benchmark_appendix(processed: dict[str, Any], report_date: str) -> str:
    other = [item for item in benchmark_items(processed) if benchmark_layer(item) == "other"]
    if not other:
        return ""
    path = benchmark_appendix_path(report_date)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Other Benchmarks - {report_date}",
        "",
        "以下条目只列标题，未在日报正文展开。",
        "",
    ]
    for item in other:
        lines.append(compact_item(item))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(path).replace("\\", "/")


def render_benchmark_section(processed: dict[str, Any], *, report_date: str, limit: int | None = None) -> str:
    shown = benchmark_items(processed)
    if not shown:
        return "- 今日无明显 benchmark / dataset / evaluation 条目。"
    core = [item for item in shown if benchmark_layer(item) == "core"][:5]
    interesting = [item for item in shown if benchmark_layer(item) == "interesting"][:5]
    other = [item for item in shown if benchmark_layer(item) == "other"]
    if limit is not None:
        core = core[:limit]
        interesting = interesting[: max(0, limit - len(core))]
    lines: list[str] = ["### Core Benchmarks for My Research"]
    lines.append(
        "\n\n".join(benchmark_block(item, idx) for idx, item in enumerate(core, 1))
        if core
        else "- 今日没有核心 benchmark。"
    )
    lines.extend(["", "### Interesting Benchmarks"])
    lines.append(
        "\n\n".join(benchmark_block(item, idx) for idx, item in enumerate(interesting, 1))
        if interesting
        else "- 今日没有额外值得展开的 benchmark。"
    )
    lines.extend(["", "### Other Benchmarks"])
    appendix = benchmark_appendix_path(report_date)
    if other:
        lines.append(f"- 其余 {len(other)} 个只进入附录标题列表：{str(appendix).replace(chr(92), '/')}")
    else:
        lines.append("- 无。")
    return "\n".join(lines)


def source_count(processed: dict[str, Any]) -> int:
    source_ids = {
        item.get("source", {}).get("id")
        for item in processed.get("items", [])
        if item.get("source", {}).get("id")
    }
    for item in processed.get("items", []):
        for source in item.get("duplicate_sources", []) or []:
            if source.get("id"):
                source_ids.add(source["id"])
    return len(source_ids)


def top_keywords(items: list[dict[str, Any]], *, limit: int = 10) -> str:
    counter: Counter[str] = Counter()
    for item in items:
        for keyword in item.get("matched_keywords", [])[:10]:
            text = str(keyword).strip()
            if text and len(text) <= 40:
                counter[text] += 1
    return "、".join(keyword for keyword, _ in counter.most_common(limit)) or "无明显集中关键词"


def section_title_from_item(item: dict[str, Any]) -> str:
    section = item.get("primary_section", {})
    return section_display_name(section.get("id", ""), section.get("title", "未分类"))


def _extract_trend_keywords(items: list[dict[str, Any]]) -> list[str]:
    keywords = []
    for item in items:
        title = item.get("title", "").lower()
        summary = item.get("summary", "").lower()
        matched_kw = [str(k).lower() for k in item.get("matched_keywords", [])]
        combined = title + " " + summary + " " + " ".join(matched_kw)
        if "agent" in combined and ("memory" in combined or "retrieval" in combined or "knowledge" in combined):
            keywords.append("Agent记忆/检索")
        if "vlm" in combined or "vision" in combined or "distill" in combined:
            keywords.append("VLM蒸馏")
        if "ranking" in combined or "clip" in combined or "dinov" in combined or "dino" in combined:
            keywords.append("多模态排序")
        if "reasoning" in combined and ("llm" in combined or "model" in combined):
            keywords.append("LLM推理")
        if "fine-tun" in combined or "lora" in combined or "parameter-eff" in combined:
            keywords.append("参数高效微调")
        if "long-context" in combined or "context-window" in combined:
            keywords.append("长上下文")
        if "reward" in combined and ("model" in combined or "rl" in combined):
            keywords.append("奖励模型/RL")
        if "world-model" in combined or "plann" in combined:
            keywords.append("世界模型/规划")
        if "multi-agent" in combined or ("multi" in combined and "agent" in combined):
            keywords.append("多智能体")
    return keywords


def _generate_trend_judgement(must: list[dict[str, Any]], direction: str) -> str:
    if not must:
        return "今天没有强制深读项，建议归档观察。"
    titles = [item.get("title", "") for item in must]
    trend_keywords = _extract_trend_keywords(must)
    unique_trends = list(dict.fromkeys(trend_keywords))
    if len(must) == 1:
        title = must[0].get("title", "")[:60]
        return f"今天仅 1 篇 Must Read——{title}。"
    if unique_trends:
        if len(unique_trends) == 1:
            return f"今天的 Must Read 集中在 {unique_trends[0]} 方向。"
        elif len(unique_trends) == 2:
            return f"今天的 Must Read 呈现 {unique_trends[0]} 和 {unique_trends[1]} 双重主线。"
        else:
            main_trends = "、".join(unique_trends[:3])
            return f"今天的 Must Read 呈现 {main_trends} 等多个研究方向。"
    return f"今天 {len(must)} 篇 Must Read，重点关注方向：{direction}。"


def build_overview(processed: dict[str, Any]) -> dict[str, Any]:
    items = processed.get("items", [])
    must = [item for item in items if item.get("reading_tier") == "MUST_READ"]
    skim = [item for item in items if item.get("reading_tier") == "SKIM"]
    watch = [item for item in items if item.get("reading_tier") == "WATCH"]
    watch_display = sorted(watch, key=score_rank, reverse=True)[:12]
    tracked = must + skim
    section_counter = Counter(section_title_from_item(item) for item in tracked or items[:20])
    direction = section_counter.most_common(1)[0][0] if section_counter else "今日信号分散"
    must_titles = "；".join(item.get("title", "") for item in must[:3])
    skim_titles = "；".join(item.get("title", "") for item in skim[:5])
    watch_titles = "；".join(item.get("title", "") for item in watch_display[:5])
    keywords = top_keywords(tracked or items, limit=8)
    judgement = _generate_trend_judgement(must, direction)
    return {
        "most_important_direction": direction,
        "must_read_count": len(must),
        "must_read_titles": must_titles,
        "skim_count": len(skim),
        "skim_titles": skim_titles,
        "watch_count": len(watch_display),
        "watch_titles": watch_titles,
        "keywords": keywords,
        "judgement": judgement,
    }



def reading_purpose(item: dict[str, Any]) -> str:
    section_id = item.get("primary_section", {}).get("id", "")
    if section_id in {"context_compression_memory", "context_compression", "context_memory"}:
        return "判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。"
    if section_id == "agents":
        return "提取 Agent 任务设定、工具使用方式、规划机制和评测指标。"
    if section_id in {"open_world_learning", "open_world"}:
        return "关注开放集/OOD/持续学习设定与可复用 benchmark。"
    if section_id in {"model_distillation", "distillation_efficiency"}:
        return "评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。"
    if item.get("is_open_source_project"):
        return "判断代码质量、复现实验入口和是否值得 clone 研读。"
    return "判断该成果与当前研究问题的连接点和是否值得进入文献库。"


def is_eligible_for_deep_read(item: dict[str, Any]) -> bool:
    """
    判断条目是否符合深读清单的要求：
    1. 必须是论文、技术报告或高质量一手研究 blog
    2. 不得是 GitHub / Open Source Projects 分类
    3. grounding_level 不能是 title_only
    """
    if item.get("is_open_source_project"):
        return False
    
    section_title = item.get("primary_category", {}).get("title", "")
    if section_title == "GitHub / Open Source Projects":
        return False
    
    ground_level = grounding_level(item)
    if ground_level == "title_only":
        return False
    
    source_type = str(item.get("source", {}).get("type", "")).lower()
    valid_types = {"arxiv", "openreview", "hf_daily_papers", "hf_papers_page"}
    
    kind = item.get("source", {}).get("kind", "")
    is_primary = kind == "primary"
    
    if source_type in valid_types or is_primary:
        return True
    
    return False


def render_deep_read_list(items: list[dict[str, Any]]) -> str:
    must_candidates = [item for item in items if item.get("reading_tier") == "MUST_READ"]
    eligible = [item for item in must_candidates if is_eligible_for_deep_read(item)][:3]
    
    if not eligible:
        return "- 今日没有符合条件的深读条目。"
    
    return "\n".join(
        f"- [{item.get('title')}]({item.get('url')})：预计阅读目的：{reading_purpose(item)}"
        for item in eligible
    )


def render_classic_revisit(classics: list[dict[str, Any]]) -> str:
    if not classics:
        return "- 今日没有足够明确的主题连接，暂不推荐经典论文。"
    lines: list[str] = []
    for idx, paper in enumerate(classics[:3], 1):
        related_sections = "、".join(paper.get("related_sections", [])) or "相关方向"
        authors = "、".join(str(author) for author in paper.get("authors", [])[:8])
        if len(paper.get("authors", [])) > 8:
            authors += " 等"
        topic_tags = "、".join(str(tag) for tag in paper.get("topic_tags", [])[:8])
        lines.append(f"### {idx}. [{paper.get('title')}]({paper.get('url')})（{paper.get('year')}）")
        lines.append(f"- 作者：{authors or '未知'}")
        lines.append(f"- topic_tags：{topic_tags or '未标注'}")
        lines.append(f"- 关联方向：{related_sections}")
        lines.append(f"- 为什么经典：{paper.get('why_classic') or paper.get('why_now')}")
        concept = paper.get("concept_connection") or {}
        if concept:
            lines.append(f"- 今日新论文继承了什么问题：{concept.get('inherits', '需要打开今日论文确认。')}")
            lines.append(f"- 它挑战了什么经典假设：{concept.get('challenges', '需要打开今日论文确认。')}")
            lines.append(f"- 它推进到什么新场景：{concept.get('extends', '需要打开今日论文确认。')}")
        else:
            lines.append(f"- 它和今日新论文的概念连接：{paper.get('modern_connection', '今天没有足够明确的新论文连接；作为基础脉络复习。')}")
        if paper.get("prerequisite"):
            lines.append(f"- 预备知识：{paper.get('prerequisite')}")
        related_today = paper.get("related_today", [])
        if related_today:
            lines.append("- 相关今日条目：")
            for item in related_today:
                terms = "、".join(item.get("connection_terms", []))
                suffix = f"；连接词：{terms}" if terms else ""
                lines.append(f"  - [{item.get('title')}]({item.get('url')})（{item.get('section')}{suffix}）")
        lines.append("")
    return "\n".join(lines).rstrip()


def previous_report_link(report_date: str) -> str:
    try:
        previous = datetime.strptime(report_date, "%Y-%m-%d") - timedelta(days=1)
    except ValueError:
        return "未知"
    previous_date = previous.strftime("%Y-%m-%d")
    previous_path = Path("reports") / "daily" / previous.strftime("%Y") / previous.strftime("%m") / f"{previous_date}.md"
    return str(previous_path).replace("\\", "/") if previous_path.exists() else f"{previous_date}：未找到上一期日报"


def build_template_context(processed: dict[str, Any], report_date: str, report_path: Path) -> dict[str, Any]:
    items = processed.get("items", [])
    collection_time = processed.get("generated_at") or datetime.now().isoformat(timespec="seconds")
    benchmark_appendix = write_benchmark_appendix(processed, report_date)
    return {
        "report_date": report_date,
        "overview": build_overview(processed),
        "primary": {
            "context_compression": render_primary_section(processed, ["context_compression_memory", "context_compression", "context_memory"]),
            "agents": render_primary_section(processed, ["agents"]),
            "open_world_learning": render_primary_section(processed, ["open_world_learning", "open_world"]),
            "model_distillation": render_primary_section(processed, ["model_distillation", "distillation_efficiency"]),
        },
        "traditional": {
            "cv": render_traditional_section(processed, "cv"),
            "nlp": render_traditional_section(processed, "nlp"),
            "rl": render_traditional_section(processed, "rl"),
            "model_architecture": render_traditional_section(processed, "model_architecture"),
            "learning_methods": render_traditional_section(processed, "learning_methods"),
        },
        "other_highlights": render_other_section(processed, ["highlights", "other_highlights"], limit=5),
        "benchmark_evaluation": render_benchmark_section(processed, report_date=report_date),
        "github_projects": render_full_items(processed.get("github_projects", []), limit=5, empty="- 今日没有进入正文的开源项目候选。"),
        "institutional_updates": render_other_section(processed, ["institutional_updates"], limit=5),
        "classic_revisit": render_classic_revisit(processed.get("classic_revisit", [])),
        "deep_read_list": render_deep_read_list(items),
        "collection": {
            "generated_at": collection_time,
            "source_count": source_count(processed),
            "raw_count": processed.get("counts", {}).get("raw", 0),
            "dedup_count": processed.get("counts", {}).get("deduped", 0),
            "summary_mode": "LLM summary mode" if openai_enabled() else "local summary mode",
            "local_summary_notice": "" if openai_enabled() else "当前为本地摘要模式，解释质量有限",
            "benchmark_appendix": benchmark_appendix,
            "report_path": str(report_path).replace("\\", "/"),
            "previous_report_link": previous_report_link(report_date),
        },
    }


def render_daily_template(context: dict[str, Any], template_path: str | Path = DEFAULT_TEMPLATE_PATH) -> str:
    path = Path(template_path)
    env = Environment(
        loader=FileSystemLoader(str(path.parent)),
        autoescape=False,
        trim_blocks=False,
        lstrip_blocks=True,
    )
    template = env.get_template(path.name)
    return template.render(**context).rstrip() + "\n"


def generate_report(
    processed: dict[str, Any] | list[dict[str, Any]],
    output: str | Path,
    *,
    report_date: str | None = None,
    latest_path: str | Path | None = "report.md",
    archive_latest: bool = True,
    generate_html: bool = True,
) -> str:
    if isinstance(processed, list):
        processed = {
            "date": report_date or datetime.now().strftime("%Y-%m-%d"),
            "counts": {"processed": len(processed)},
            "sections": [{"title": "Legacy Ranked Items", "group": "core_focus", "items": processed}],
            "github_projects": [],
            "classic_revisit": [],
            "items": processed,
        }

    report_date = report_date or processed.get("date") or datetime.now().strftime("%Y-%m-%d")
    output_path = Path(output)
    context = build_template_context(processed, report_date, output_path)
    rendered = render_daily_template(context)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")

    # Archive previous latest.md before overwriting
    if archive_latest and latest_path and Path(latest_path).exists():
        archive_report_with_timestamp(
            latest_path,
            archive_dir="reports/history",
            suffix="latest",
        )

    if latest_path:
        shutil.copyfile(output_path, latest_path)

    # Auto-generate HTML from the generated Markdown
    if generate_html:
        try:
            html_path = generate_html_report(output_path)
            print(f"Generated HTML report: {html_path}")

            # Also generate HTML for report.md (root level)
            if latest_path and Path(latest_path).exists():
                root_html_path = Path("report.html")
                generate_html_report(latest_path, root_html_path)
                print(f"Generated root HTML report: {root_html_path}")
        except Exception as e:
            print(f"HTML generation warning: {e}")

    return rendered


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Chinese Markdown dashboard report.")
    parser.add_argument("--input", default="data/processed.json")
    parser.add_argument("--output", default=None)
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"))
    args = parser.parse_args()

    output = args.output or f"reports/daily/{args.date[:4]}/{args.date[5:7]}/{args.date}.md"
    processed = load_json(args.input)
    generate_report(processed, output, report_date=args.date)
    print(f"wrote report to {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
