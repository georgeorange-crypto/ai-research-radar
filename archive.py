from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from typing import Any


def load_json(path: str | Path) -> Any:
    with open(path, "r", encoding="utf-8-sig") as f:
        return json.load(f)


def parse_day(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def month_id(day: date) -> str:
    return day.strftime("%Y-%m")


def processed_files(processed_dir: str | Path = "data/processed") -> list[Path]:
    paths: list[Path] = []
    for path in Path(processed_dir).glob("*.json"):
        try:
            parse_day(path.stem)
        except ValueError:
            continue
        paths.append(path)
    return sorted(paths)


def processed_files_for_month(processed_dir: str | Path, day: date) -> list[Path]:
    mid = month_id(day)
    return [path for path in processed_files(processed_dir) if path.stem.startswith(mid)]


def daily_report_path(report_date: str) -> Path:
    year, month, _ = report_date.split("-")
    return Path("reports") / "daily" / year / month / f"{report_date}.md"


def relative_link(from_file: str | Path, target: str | Path) -> str:
    base = Path(from_file).parent
    try:
        return Path(target).resolve().relative_to(base.resolve()).as_posix()
    except ValueError:
        return Path(target).as_posix()


def score_rank(item: dict[str, Any]) -> tuple[float, float, float]:
    scores = item.get("scores", {})
    return (
        scores.get("personal_score", scores.get("overall", 0)),
        scores.get("global_score", scores.get("overall", 0)),
        scores.get("research_relevance", scores.get("relevance", 0)),
    )


def tracked_items(report: dict[str, Any]) -> list[dict[str, Any]]:
    return [item for item in report.get("items", []) if item.get("reading_tier") != "IGNORE"]


def unique_items(reports: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_key: dict[str, dict[str, Any]] = {}
    for report in reports:
        for item in tracked_items(report):
            key = item.get("id") or item.get("url") or item.get("title")
            existing = by_key.get(key)
            if not existing or score_rank(item) > score_rank(existing):
                by_key[key] = item
    return sorted(by_key.values(), key=score_rank, reverse=True)


def main_direction(report: dict[str, Any]) -> str:
    candidates = [
        item
        for item in report.get("items", [])
        if item.get("reading_tier") in {"MUST_READ", "SKIM"}
    ]
    if not candidates:
        candidates = tracked_items(report)[:30]
    counter: Counter[str] = Counter()
    for item in candidates:
        section = item.get("primary_section", {})
        title = section.get("title") or section.get("id") or "未分类"
        counter[str(title)] += 1
    return counter.most_common(1)[0][0] if counter else "无明显主方向"


def must_read_count(report: dict[str, Any]) -> int:
    counts = report.get("counts", {})
    if "must_read" in counts:
        return int(counts.get("must_read") or 0)
    return sum(1 for item in report.get("items", []) if item.get("reading_tier") == "MUST_READ")


def compact_item(item: dict[str, Any]) -> str:
    scores = item.get("scores", {})
    tier = item.get("reading_tier", "ARCHIVE")
    section = item.get("primary_section", {}).get("title", "未分类")
    score = scores.get("personal_score", scores.get("overall", 0))
    return f"- [{item.get('title')}]({item.get('url')})（{tier}，{section}，score {score:.2f}）"


def trend_sentence(section_title: str, items: list[dict[str, Any]]) -> str:
    keywords: Counter[str] = Counter()
    for item in items:
        for keyword in item.get("matched_keywords", [])[:8]:
            cleaned = re.sub(r"\s+", " ", str(keyword)).strip()
            if cleaned:
                keywords[cleaned] += 1
    top_keywords = "、".join(keyword for keyword, _ in keywords.most_common(8)) or "主题较分散"
    return f"- {section_title}：{len(items)} 条进入跟踪；高频信号：{top_keywords}。"


def generate_monthly_report(
    processed_dir: str | Path = "data/processed",
    output: str | Path | None = None,
    *,
    report_date: str | None = None,
    latest_path: str | Path | None = "reports/monthly/latest.md",
) -> str:
    day = parse_day(report_date) if report_date else date.today()
    mid = month_id(day)
    output_path = Path(output) if output else Path("reports") / "monthly" / f"{mid}.md"
    paths = processed_files_for_month(processed_dir, day)
    reports = [load_json(path) for path in paths]
    items = unique_items(reports)

    tier_counts = Counter(item.get("reading_tier", "ARCHIVE") for item in items)
    direction_counter = Counter(main_direction(report) for report in reports)
    section_map: dict[str, list[dict[str, Any]]] = {}
    for item in items:
        section = item.get("primary_section", {}).get("title", "未分类")
        section_map.setdefault(section, []).append(item)

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

    lines = [
        f"# AI Research Radar Monthly - {mid}",
        "",
        f"- 纳入日报：{len(paths)} 份",
        f"- 跟踪条目：{len(items)}；MUST_READ {tier_counts.get('MUST_READ', 0)}；SKIM {tier_counts.get('SKIM', 0)}；ARCHIVE {tier_counts.get('ARCHIVE', 0)}",
        f"- 本月高频主方向：{direction_counter.most_common(1)[0][0] if direction_counter else '无'}",
        "",
        "## 本月最重要论文 / 动态",
    ]

    if items:
        for item in items[:20]:
            lines.append(compact_item(item))
    else:
        lines.append("- 本月还没有 processed 数据。")

    lines.extend(["", "## 分方向趋势"])
    for section_title, section_items in sorted(section_map.items(), key=lambda pair: len(pair[1]), reverse=True):
        lines.append(trend_sentence(section_title, section_items))
        for item in sorted(section_items, key=score_rank, reverse=True)[:5]:
            lines.append(f"  - [{item.get('title')}]({item.get('url')})")

    lines.extend(["", "## GitHub / 开源项目"])
    if github_projects:
        for item in github_projects[:15]:
            metrics = item.get("metrics", {})
            stars = metrics.get("stars")
            suffix = f"，stars {stars}" if stars is not None else ""
            lines.append(f"- [{item.get('title')}]({item.get('url')})（{item.get('primary_section', {}).get('title', '未分类')}{suffix}）")
    else:
        lines.append("- 本月没有进入跟踪队列的开源项目。")

    lines.extend(["", "## 月度判断"])
    if section_map:
        for section_title, section_items in sorted(section_map.items(), key=lambda pair: len(pair[1]), reverse=True)[:6]:
            top = sorted(section_items, key=score_rank, reverse=True)[0]
            lines.append(f"- {section_title}：本月可继续沿着 [{top.get('title')}]({top.get('url')}) 追踪。")
    else:
        lines.append("- 等待更多日报数据后生成月度判断。")
    lines.append("")

    rendered = "\n".join(lines)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")
    if latest_path:
        Path(latest_path).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(output_path, latest_path)
    return rendered


def generate_index(
    processed_dir: str | Path = "data/processed",
    output: str | Path = "reports/index.md",
) -> str:
    output_path = Path(output)
    entries: list[dict[str, Any]] = []
    for path in processed_files(processed_dir):
        report = load_json(path)
        report_date = report.get("date") or path.stem
        daily_path = daily_report_path(report_date)
        entries.append(
            {
                "date": report_date,
                "must_read": must_read_count(report),
                "main_direction": main_direction(report),
                "daily_path": daily_path,
            }
        )

    entries.sort(key=lambda entry: entry["date"], reverse=True)
    lines = [
        "# AI Research Radar Index",
        "",
        "| 日期 | 今日 Must Read 数量 | 今日主要方向 | 链接 |",
        "|---|---:|---|---|",
    ]
    for entry in entries:
        link = relative_link(output_path, entry["daily_path"])
        label = Path(entry["daily_path"]).name
        lines.append(
            f"| {entry['date']} | {entry['must_read']} | {entry['main_direction']} | [{label}]({link}) |"
        )
    if not entries:
        lines.append("| 暂无 | 0 | 无 | - |")
    lines.append("")

    rendered = "\n".join(lines)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")
    return rendered


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate monthly reports and the report index.")
    parser.add_argument("--processed-dir", default="data/processed")
    parser.add_argument("--date", default=date.today().strftime("%Y-%m-%d"))
    parser.add_argument("--monthly-output", default=None)
    parser.add_argument("--index-output", default="reports/index.md")
    parser.add_argument("--skip-monthly", action="store_true")
    parser.add_argument("--skip-index", action="store_true")
    args = parser.parse_args()

    if not args.skip_monthly:
        day = parse_day(args.date)
        output = args.monthly_output or Path("reports") / "monthly" / f"{month_id(day)}.md"
        generate_monthly_report(args.processed_dir, output, report_date=args.date)
        print(f"wrote monthly report for {month_id(day)}")
    if not args.skip_index:
        generate_index(args.processed_dir, args.index_output)
        print(f"wrote index to {args.index_output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
