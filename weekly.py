from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

TIER_RANK = {"MUST_READ": 3, "SKIM": 2, "WATCH": 1, "ARCHIVE": 0}


def load_json(path: str | Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def week_id(day: date) -> str:
    iso = day.isocalendar()
    return f"{iso.year}-W{iso.week:02d}"


def parse_day(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def week_bounds(day: date) -> tuple[date, date]:
    start = day - timedelta(days=day.weekday())
    return start, start + timedelta(days=6)


def processed_files_for_week(processed_dir: str | Path, day: date) -> list[Path]:
    start, end = week_bounds(day)
    paths = []
    for path in Path(processed_dir).glob("*.json"):
        try:
            file_day = parse_day(path.stem)
        except ValueError:
            continue
        if start <= file_day <= end:
            paths.append(path)
    return sorted(paths)


def unique_items(reports: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_key: dict[str, dict[str, Any]] = {}
    for report in reports:
        for item in report.get("items", []):
            if item.get("reading_tier") == "IGNORE":
                continue
            key = item.get("id") or item.get("url") or item.get("title")
            existing = by_key.get(key)
            if not existing or report_rank(item) > report_rank(existing):
                by_key[key] = item
    return list(by_key.values())


def score_rank(item: dict[str, Any]) -> tuple[float, float, float]:
    scores = item.get("scores", {})
    return (
        scores.get("personal_score", 0),
        scores.get("research_relevance", 0),
        scores.get("global_score", 0),
    )


def report_rank(item: dict[str, Any]) -> tuple[int, float, float, float]:
    return (TIER_RANK.get(item.get("reading_tier", "ARCHIVE"), -1), *score_rank(item))


def sorted_for_report(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(items, key=report_rank, reverse=True)


def compact_item(item: dict[str, Any]) -> str:
    scores = item.get("scores", {})
    tier = item.get("reading_tier", "ARCHIVE")
    section = item.get("primary_section", {}).get("title", "未分类")
    return (
        f"- [{item.get('title')}]({item.get('url')})"
        f"（{tier}，{section}，personal {scores.get('personal_score', 0):.2f}，global {scores.get('global_score', 0):.2f}）"
    )


def trend_sentence(section_title: str, items: list[dict[str, Any]]) -> str:
    keywords = Counter()
    for item in items:
        for keyword in item.get("matched_keywords", [])[:8]:
            cleaned = re.sub(r"\s+", " ", str(keyword)).strip()
            if cleaned:
                keywords[cleaned] += 1
    top_keywords = "、".join(keyword for keyword, _ in keywords.most_common(6)) or "主题较分散"
    return f"- {section_title}：{len(items)} 条进入跟踪；高频信号：{top_keywords}。"


def generate_weekly_report(
    processed_dir: str | Path = "data/processed",
    output: str | Path | None = None,
    *,
    report_date: str | None = None,
    latest_path: str | Path | None = "reports/weekly/latest.md",
) -> str:
    day = parse_day(report_date) if report_date else date.today()
    wid = week_id(day)
    output_path = Path(output) if output else Path("reports") / "weekly" / f"{wid}.md"
    paths = processed_files_for_week(processed_dir, day)
    reports = [load_json(path) for path in paths]
    items = unique_items(reports)
    items.sort(key=report_rank, reverse=True)

    section_map: dict[str, list[dict[str, Any]]] = {}
    for item in items:
        title = item.get("primary_section", {}).get("title", "未分类")
        section_map.setdefault(title, []).append(item)

    github_projects = [item for item in items if item.get("is_open_source_project")]
    github_projects.sort(
        key=lambda item: (
            item.get("source", {}).get("type") == "github_search",
            item.get("scores", {}).get("actionability", 0),
            item.get("scores", {}).get("community_signal", 0),
            item.get("metrics", {}).get("stars", 0) or 0,
        ),
        reverse=True,
    )

    tier_counts = Counter(item.get("reading_tier", "ARCHIVE") for item in items)
    start, end = week_bounds(day)
    lines = [
        f"# AI Research Radar Weekly - {wid}",
        "",
        f"- 日期范围：{start.isoformat()} 至 {end.isoformat()}",
        f"- 纳入日报：{len(paths)} 份",
        f"- 跟踪条目：{len(items)}；MUST_READ {tier_counts.get('MUST_READ', 0)}；SKIM {tier_counts.get('SKIM', 0)}；ARCHIVE {tier_counts.get('ARCHIVE', 0)}",
        "",
        "## 本周最重要论文 / 动态",
    ]

    if items:
        for item in items[:12]:
            lines.append(compact_item(item))
    else:
        lines.append("- 本周还没有 processed 数据。")

    lines.extend(["", "## 分方向趋势"])
    for section_title, section_items in sorted(section_map.items(), key=lambda pair: len(pair[1]), reverse=True):
        lines.append(trend_sentence(section_title, section_items))
        for item in sorted_for_report(section_items)[:5]:
            lines.append(f"  - [{item.get('title')}]({item.get('url')})")

    lines.extend(["", "## GitHub / Open-source Projects"])
    if github_projects:
        for item in github_projects[:5]:
            metrics = item.get("metrics", {})
            stars = metrics.get("stars")
            suffix = f"，stars {stars}" if stars is not None else ""
            lines.append(f"- [{item.get('title')}]({item.get('url')})（{item.get('primary_section', {}).get('title', '未分类')}{suffix}）")
    else:
        lines.append("- 本周没有进入跟踪队列的开源项目。")

    lines.extend(["", "## 下周跟踪建议"])
    if section_map:
        for section_title, section_items in sorted(section_map.items(), key=lambda pair: len(pair[1]), reverse=True)[:5]:
            top = sorted_for_report(section_items)[0]
            lines.append(f"- 继续跟踪 {section_title}：本周最强信号是 [{top.get('title')}]({top.get('url')})。")
    else:
        lines.append("- 等待更多日报数据后生成趋势判断。")
    lines.append("")

    rendered = "\n".join(lines)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")
    if latest_path:
        Path(latest_path).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(output_path, latest_path)
    return rendered


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a weekly AI research radar report.")
    parser.add_argument("--processed-dir", default="data/processed")
    parser.add_argument("--output", default=None)
    parser.add_argument("--date", default=date.today().strftime("%Y-%m-%d"))
    args = parser.parse_args()

    generate_weekly_report(args.processed_dir, args.output, report_date=args.date)
    print(f"wrote weekly report for {week_id(parse_day(args.date))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
