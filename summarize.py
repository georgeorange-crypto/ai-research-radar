from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import requests


KIND_LABELS = {
    "primary": "一手来源",
    "aggregator": "聚合/摘要",
    "media": "媒体摘要",
}


def load_json(path: str | Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def trim(text: str, limit: int = 360) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def cn_bool(value: bool) -> str:
    return "是" if value else "否"


def fallback_summary(item: dict[str, Any]) -> dict[str, Any]:
    focus = "、".join(item.get("matched_focus_areas", [])[:4]) or "你的重点方向"
    source_kind = item.get("source", {}).get("kind", "primary")
    summary_text = trim(item.get("summary", ""), 300)
    if summary_text:
        summary = f"该条目围绕“{item.get('title')}”展开，原始摘要显示其主要内容是：{summary_text}"
    else:
        summary = f"该条目围绕“{item.get('title')}”展开，当前源没有提供足够摘要，需要打开原文确认细节。"

    why = f"它与 {focus} 相关；来源类型为{KIND_LABELS.get(source_kind, source_kind)}，适合用于日常雷达跟踪。"
    if item.get("scores", {}).get("actionability", 0) >= 0.65:
        why += " 其中包含较强的可操作信号，例如代码、数据、评测、系统或方法线索。"

    deep_read = item.get("worth_deep_read", False)
    reason = "综合相关性、可信度和新颖性较高。" if deep_read else "可先扫读，除非它正好命中当前课题。"
    return {
        "summary": summary,
        "importance": why,
        "deep_read": deep_read,
        "deep_read_reason": reason,
    }


def openai_enabled() -> bool:
    return bool(os.getenv("OPENAI_API_KEY"))


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
        "matched_focus_areas": item.get("matched_focus_areas", []),
        "matched_keywords": item.get("matched_keywords", []),
        "scores": item.get("scores", {}),
        "worth_deep_read": item.get("worth_deep_read", False),
    }
    messages = [
        {
            "role": "system",
            "content": (
                "你是严谨的 AI research radar 编辑。用中文输出，不夸张，不营销。"
                "只基于输入信息总结；信息不足时明确说需要打开原文确认。"
                "返回严格 JSON，字段为 summary, importance, deep_read, deep_read_reason。"
            ),
        },
        {
            "role": "user",
            "content": json.dumps(prompt, ensure_ascii=False),
        },
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
        content = response.json()["choices"][0]["message"]["content"]
        parsed = json.loads(content)
        if all(key in parsed for key in ["summary", "importance", "deep_read", "deep_read_reason"]):
            return parsed
    except Exception:
        return None
    return None


def item_block(item: dict[str, Any], idx: int, summary: dict[str, Any]) -> str:
    source = item.get("source", {})
    kind = source.get("kind", "primary")
    scores = item.get("scores", {})
    published = item.get("published_at") or "未知"
    duplicated = item.get("duplicate_sources") or []
    duplicate_names = sorted({s.get("name", "") for s in duplicated if s.get("name")})
    duplicate_text = "、".join(duplicate_names[:5]) if len(duplicate_names) > 1 else ""
    keywords = "、".join(item.get("matched_keywords", [])[:10]) or "无明显关键词"
    focus = "、".join(item.get("matched_focus_areas", [])[:5]) or "未命中重点方向"
    deep_read = bool(summary.get("deep_read", item.get("worth_deep_read", False)))

    lines = [
        f"### {idx}. [{item.get('title')}]({item.get('url')})",
        f"- 来源：{source.get('name', '未知')}",
        f"- 来源类型：{KIND_LABELS.get(kind, kind)}",
        f"- 原文链接：{item.get('url')}",
        f"- 发布时间：{published}",
        f"- 简明摘要：{summary.get('summary', '').strip()}",
        f"- 为什么重要：{summary.get('importance', '').strip()}",
        f"- 是否值得深读：{cn_bool(deep_read)}。{summary.get('deep_read_reason', '').strip()}",
        (
            "- 评分："
            f"relevance {scores.get('relevance', 0):.2f}；"
            f"credibility {scores.get('credibility', 0):.2f}；"
            f"novelty {scores.get('novelty', 0):.2f}；"
            f"actionability {scores.get('actionability', 0):.2f}；"
            f"overall {scores.get('overall', 0):.2f}"
        ),
        f"- 命中方向：{focus}",
        f"- 命中关键词：{keywords}",
    ]
    if duplicate_text:
        lines.append(f"- 去重信息：同一内容也出现在 {duplicate_text}")
    return "\n".join(lines)


def generate_report(
    ranked_items: list[dict[str, Any]],
    output: str | Path,
    *,
    report_date: str | None = None,
    max_items: int = 35,
    latest_path: str | Path | None = "report.md",
) -> str:
    report_date = report_date or datetime.now().strftime("%Y-%m-%d")
    selected = ranked_items[:max_items]
    summarized: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for item in selected:
        summary = summarize_with_openai(item) if openai_enabled() else None
        summarized.append((item, summary or fallback_summary(item)))

    primary = [(item, s) for item, s in summarized if item.get("source", {}).get("kind") == "primary"]
    secondary = [(item, s) for item, s in summarized if item.get("source", {}).get("kind") != "primary"]
    deep_reads = [item for item, summary in summarized if summary.get("deep_read", item.get("worth_deep_read", False))]

    lines = [
        f"# AI Research Radar - {report_date}",
        "",
        f"- 生成时间：{datetime.now().isoformat(timespec='seconds')}",
        f"- 条目数：{len(selected)} / 抓取后排序总数 {len(ranked_items)}",
        f"- 值得深读：{len(deep_reads)}",
        f"- 摘要模式：{'OpenAI API 中文摘要' if openai_enabled() else '本地规则摘要（未配置 OPENAI_API_KEY）'}",
        "",
        "## 阅读建议",
    ]

    if deep_reads:
        for item in deep_reads[:8]:
            score = item.get("scores", {}).get("overall", 0)
            lines.append(f"- [{item.get('title')}]({item.get('url')})（overall {score:.2f}）")
    else:
        lines.append("- 今天没有明显高优先级条目，可扫读排名靠前内容。")

    lines.extend(["", "## 一手来源"])
    if primary:
        for idx, (item, summary) in enumerate(primary, 1):
            lines.append(item_block(item, idx, summary))
            lines.append("")
    else:
        lines.append("- 今日未抓取到一手来源条目。")
        lines.append("")

    lines.append("## 媒体摘要与聚合")
    if secondary:
        for idx, (item, summary) in enumerate(secondary, 1):
            lines.append(item_block(item, idx, summary))
            lines.append("")
    else:
        lines.append("- 今日未抓取到媒体摘要或聚合条目。")
        lines.append("")

    lines.extend(
        [
            "## 采集说明",
            "- 已按 arXiv/OpenReview 论文 ID、URL 和规范化标题自动去重。",
            "- 一手来源包括论文平台、官方机构、官方实验室和会议站点；媒体摘要与聚合包括新闻信、趋势榜和每日论文聚合。",
            "- 评分仅用于排序和筛选，不代表论文质量定论。",
            "",
        ]
    )

    rendered = "\n".join(lines)
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")
    if latest_path:
        shutil.copyfile(output_path, latest_path)
    return rendered


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Chinese Markdown research report.")
    parser.add_argument("--input", default="data/ranked.json")
    parser.add_argument("--output", default=None)
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--max-items", type=int, default=int(os.getenv("RADAR_MAX_REPORT_ITEMS", "35")))
    args = parser.parse_args()

    output = args.output or f"reports/{args.date}.md"
    ranked = load_json(args.input)
    generate_report(ranked, output, report_date=args.date, max_items=args.max_items)
    print(f"wrote report to {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
