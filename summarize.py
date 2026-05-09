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
from jinja2 import Environment, FileSystemLoader


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
    "ARCHIVE": "ARCHIVE",
    "IGNORE": "IGNORE",
}

SUMMARY_FIELDS = [
    "what_is_it",
    "problem",
    "method_or_contribution",
    "why_important",
    "deep_read",
    "suggested_action",
]

ACTION_CHOICES = {"read_pdf", "skim", "save", "reproduce", "ignore"}
DEFAULT_TEMPLATE_PATH = Path("config") / "daily_report.md.j2"

SECTION_DISPLAY_NAMES = {
    "context_compression": "上下文压缩 / 长上下文 / 记忆",
    "context_memory": "上下文压缩 / 长上下文 / 记忆",
    "agents": "Agent / Tool Use / Planning",
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


def choose_action(item: dict[str, Any]) -> str:
    tier = item.get("reading_tier", "ARCHIVE")
    scores = item.get("scores", {})
    if tier == "IGNORE":
        return "ignore"
    if item.get("is_open_source_project") and scores.get("actionability", 0) >= 0.70:
        return "reproduce"
    if tier == "MUST_READ":
        return "read_pdf"
    if tier == "SKIM":
        return "skim"
    return "save"


def normalize_action(value: Any, item: dict[str, Any]) -> str:
    action = str(value or "").strip().lower()
    return action if action in ACTION_CHOICES else choose_action(item)


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


def fallback_summary(item: dict[str, Any]) -> dict[str, Any]:
    section = item.get("primary_section", {}).get("title", "相关方向")
    tier = item.get("reading_tier", "ARCHIVE")
    scores = item.get("scores", {})
    summary_text = trim(item.get("summary", ""), 420)
    keywords = "、".join(item.get("matched_keywords", [])[:5])
    source_name = item.get("source", {}).get("name") or "当前来源"
    title = item.get("title") or "未命名条目"

    if summary_text:
        what_is_it = f"围绕“{title}”的研究或项目线索，原始摘要核心信息是：{summary_text}"
    else:
        what_is_it = f"围绕“{title}”的条目，但来源没有给出足够摘要，需要打开原文确认。"

    if keywords:
        problem = f"它主要落在“{section}”，关键词显示关注 {keywords} 等问题。"
    else:
        problem = f"它被归到“{section}”，但标题和摘要中的问题信号还不够明确。"

    method_or_contribution = "本地摘要无法可靠抽取完整方法细节；建议以标题、摘要和原文为准。"
    if item.get("is_open_source_project"):
        method_or_contribution = "条目带有代码或开源信号，可能包含可直接查看的实现、工具或复现实验。"
    elif summary_text:
        method_or_contribution = "可从摘要中先判断研究对象、实验设置和声称贡献，具体技术路线仍需读原文确认。"

    importance_parts = []
    if tier == "MUST_READ":
        importance_parts.append("它已进入 MUST_READ，说明个人优先级足够高，值得今天安排深读。")
    elif tier == "SKIM":
        importance_parts.append("它进入 SKIM，适合快速扫读后决定是否升级为深读。")
    elif tier == "ARCHIVE":
        importance_parts.append("它还没到深读/略读阈值，但有保留价值。")
    else:
        importance_parts.append("它目前不适合进入正文阅读队列。")

    importance_parts.append(
        f"personal_score={scores.get('personal_score', 0):.2f}，research_relevance={scores.get('research_relevance', 0):.2f}。"
    )
    if item.get("is_open_source_project"):
        importance_parts.append("开源信号让它更适合后续复现或拆代码。")

    action = choose_action(item)
    deep_read = "建议深读。" if action == "read_pdf" else "暂不建议深读，先快速判断或保存。"
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
    prompt = {
        "title": item.get("title"),
        "source": item.get("source", {}),
        "url": item.get("url"),
        "abstract_or_excerpt": trim(item.get("summary", ""), 1800),
        "primary_section": item.get("primary_section", {}),
        "matched_sections": item.get("matched_sections", []),
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
            "suggested_action": "建议行动，只能是 read_pdf / skim / save / reproduce / ignore 之一",
        },
    }
    messages = [
        {
            "role": "system",
            "content": (
                "你是严谨的 AI research radar 编辑，面向一位关注长上下文、Agent、开放世界学习和模型压缩的研究者。"
                "用自然、具体、克制的中文写摘要，不营销，不编造，不重复套话。"
                "只基于输入信息；信息不足时直接说明需要打开原文确认。"
                "避免模板化表达，不要按来源类型写泛泛的跟踪价值判断。"
                "返回严格 JSON，字段必须且只能包含："
                "what_is_it, problem, method_or_contribution, why_important, deep_read, suggested_action。"
                "suggested_action 只能是 read_pdf、skim、save、reproduce、ignore 之一。"
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
            timeout=45,
        )
        response.raise_for_status()
        parsed = json.loads(response.json()["choices"][0]["message"]["content"])
        if all(key in parsed for key in SUMMARY_FIELDS):
            return normalize_summary(parsed, item)
    except Exception:
        return None
    return None


def summarize_item(item: dict[str, Any]) -> dict[str, Any]:
    if openai_enabled():
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
    focus = "、".join(item.get("matched_focus_areas", [])[:5]) or item.get("primary_section", {}).get("title", "未分类")
    duplicate_names = sorted({s.get("name", "") for s in item.get("duplicate_sources", []) if s.get("name")})
    duplicate_text = "、".join(duplicate_names[:5]) if len(duplicate_names) > 1 else ""
    summary = summarize_item(item)

    lines = [
        f"##### {idx}. [{item.get('title')}]({item.get('url')})",
        f"- 阅读层级：{TIER_LABELS.get(item.get('reading_tier'), item.get('reading_tier', 'ARCHIVE'))}",
        f"- 来源：{source.get('name', '未知')}",
        f"- 来源类型：{KIND_LABELS.get(kind, kind)}",
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
        f"- 命中关键词：{keywords}",
    ]
    if item.get("is_open_source_project"):
        metrics = item.get("metrics", {})
        if metrics.get("stars") is not None:
            lines.append(f"- 开源信号：stars {metrics.get('stars', 0)}；forks {metrics.get('forks', 0)}；language {metrics.get('language') or '未知'}")
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
        f"（{tier}，{section}，personal {scores.get('personal_score', 0):.2f}，global {scores.get('global_score', 0):.2f}）"
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


def render_archive_titles(items: list[dict[str, Any]], limit: int = 8) -> list[str]:
    if not items:
        return []
    lines = ["", "归档候选："]
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
            lines.extend(render_archive_titles(archive_items))
            continue

        if group in {"traditional_ai", "traditional_fields"}:
            shown_items = (must_items + skim_items + archive_items)[:2]
        elif group == "other" or section_id == "highlights":
            shown_items = (must_items + skim_items + archive_items)[:5]
        else:
            shown_items = must_items + skim_items + archive_items

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
                f"- 它和今日新论文的连接：{paper.get('modern_connection', '今天没有足够明确的新论文连接；作为基础脉络复习。')}",
            ]
        )
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
        "archive": render_compact_items(items_by_tier(items, "ARCHIVE"), limit=8),
    }


def render_traditional_section(processed: dict[str, Any], section_id: str) -> str:
    items = items_for_section(processed, [section_id])
    shown = items_by_tier(items, "MUST_READ") + items_by_tier(items, "SKIM") + items_by_tier(items, "ARCHIVE")
    return render_compact_items(shown, limit=2, empty="- 今日无明显条目。")


def render_other_section(processed: dict[str, Any], section_ids: list[str], *, limit: int = 5) -> str:
    items = items_for_section(processed, section_ids)
    shown = items_by_tier(items, "MUST_READ") + items_by_tier(items, "SKIM") + items_by_tier(items, "ARCHIVE")
    return render_full_items(shown, limit=limit, empty="- 今日无明显条目。")


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


def build_overview(processed: dict[str, Any]) -> dict[str, Any]:
    items = processed.get("items", [])
    must = [item for item in items if item.get("reading_tier") == "MUST_READ"]
    skim = [item for item in items if item.get("reading_tier") == "SKIM"]
    tracked = must + skim
    section_counter = Counter(section_title_from_item(item) for item in tracked or items[:20])
    direction = section_counter.most_common(1)[0][0] if section_counter else "今日信号分散"
    must_titles = "；".join(item.get("title", "") for item in must[:3])
    skim_titles = "；".join(item.get("title", "") for item in skim[:5])
    keywords = top_keywords(tracked or items, limit=8)
    if must:
        judgement = f"今天优先围绕“{direction}”深读，先处理 MUST_READ，再把 SKIM 中与当前课题直接相关的条目升级。"
    elif skim:
        judgement = f"今天没有强制深读项，建议围绕“{direction}”快速扫读，保留可复现或可引用线索。"
    else:
        judgement = "今天没有明显高优先级条目，日报主要用于归档和趋势观察。"
    return {
        "most_important_direction": direction,
        "must_read_count": len(must),
        "must_read_titles": must_titles,
        "skim_count": len(skim),
        "skim_titles": skim_titles,
        "keywords": keywords,
        "judgement": judgement,
    }


def reading_purpose(item: dict[str, Any]) -> str:
    section_id = item.get("primary_section", {}).get("id", "")
    if section_id in {"context_compression", "context_memory"}:
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


def render_deep_read_list(items: list[dict[str, Any]]) -> str:
    must = [item for item in items if item.get("reading_tier") == "MUST_READ"][:3]
    if not must:
        return "- 今日没有 MUST_READ 条目。"
    return "\n".join(
        f"- [{item.get('title')}]({item.get('url')})：预计阅读目的：{reading_purpose(item)}"
        for item in must
    )


def render_classic_revisit(classics: list[dict[str, Any]]) -> str:
    if not classics:
        return "- 今日没有足够明确的主题连接，暂不推荐经典论文。"
    lines: list[str] = []
    for idx, paper in enumerate(classics[:2], 1):
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
        lines.append(f"- 它和今日新论文的连接：{paper.get('modern_connection', '今天没有足够明确的新论文连接；作为基础脉络复习。')}")
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
    return {
        "report_date": report_date,
        "overview": build_overview(processed),
        "primary": {
            "context_compression": render_primary_section(processed, ["context_compression", "context_memory"]),
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
    if latest_path:
        shutil.copyfile(output_path, latest_path)
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
