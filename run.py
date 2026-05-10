from __future__ import annotations

import argparse
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

try:
    from dotenv import load_dotenv
    # 自动加载 .env 文件（如果存在）
    load_dotenv()
except ImportError:
    pass

from archive import generate_index, generate_monthly_report, month_id
from fetch import configure_logging, fetch_all, save_jsonl
from rank import process_items, save_json
from summarize import generate_report
from weekly import generate_weekly_report, week_id


def today(tz_name: str) -> str:
    return datetime.now(ZoneInfo(tz_name)).strftime("%Y-%m-%d")


def daily_report_path(report_date: str) -> Path:
    year, month, _ = report_date.split("-")
    return Path("reports") / "daily" / year / month / f"{report_date}.md"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the AI research radar pipeline.")
    parser.add_argument("--date", default=None)
    parser.add_argument("--timezone", default=os.getenv("RADAR_TIMEZONE", "Asia/Shanghai"))
    parser.add_argument("--sources", default="config/sources.yaml")
    parser.add_argument("--keywords", default="config/keywords.yaml")
    parser.add_argument("--rank-limit", type=int, default=int(os.getenv("RADAR_RANK_LIMIT", "0")))
    parser.add_argument("--skip-weekly", action="store_true")
    parser.add_argument("--skip-monthly", action="store_true")
    parser.add_argument("--skip-index", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    configure_logging(args.verbose)
    report_date = args.date or today(args.timezone)
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    Path("reports/daily").mkdir(parents=True, exist_ok=True)
    Path("reports/weekly").mkdir(parents=True, exist_ok=True)
    Path("reports/monthly").mkdir(parents=True, exist_ok=True)

    raw_path = Path("data") / "raw" / f"{report_date}.jsonl"
    processed_path = Path("data") / "processed" / f"{report_date}.json"
    report_path = daily_report_path(report_date)

    raw_items = fetch_all(args.sources)
    save_jsonl(raw_path, raw_items)

    rank_limit = args.rank_limit if args.rank_limit > 0 else None
    processed = process_items(
        raw_items,
        args.keywords,
        report_date=report_date,
        limit=rank_limit,
    )
    save_json(processed_path, processed)

    generate_report(
        processed,
        report_path,
        report_date=report_date,
        latest_path=Path("reports") / "daily" / "latest.md",
    )
    shutil.copyfile(report_path, "report.md")

    weekly_path = None
    run_day = datetime.strptime(report_date, "%Y-%m-%d").date()
    if not args.skip_weekly:
        current_week = week_id(run_day)
        weekly_path = Path("reports") / "weekly" / f"{current_week}.md"
        generate_weekly_report(
            "data/processed",
            weekly_path,
            report_date=report_date,
            latest_path=Path("reports") / "weekly" / "latest.md",
        )

    monthly_path = None
    if not args.skip_monthly:
        current_month = month_id(run_day)
        monthly_path = Path("reports") / "monthly" / f"{current_month}.md"
        generate_monthly_report(
            "data/processed",
            monthly_path,
            report_date=report_date,
            latest_path=Path("reports") / "monthly" / "latest.md",
        )

    index_path = None
    if not args.skip_index:
        index_path = Path("reports") / "index.md"
        generate_index("data/processed", index_path)

    counts = processed.get("counts", {})
    print(f"raw items: {len(raw_items)}")
    print(f"processed items: {counts.get('processed', 0)}")
    print(
        "tiers: "
        f"MUST_READ={counts.get('must_read', 0)}, "
        f"SKIM={counts.get('skim', 0)}, "
        f"WATCH={counts.get('watch', 0)}, "
        f"ARCHIVE={counts.get('archive', 0)}, "
        f"IGNORE={counts.get('ignore', 0)}"
    )
    print(f"raw: {raw_path}")
    print(f"processed: {processed_path}")
    print(f"daily report: {report_path}")
    print("daily latest: reports\\daily\\latest.md")
    if weekly_path:
        print(f"weekly report: {weekly_path}")
    if monthly_path:
        print(f"monthly report: {monthly_path}")
    if index_path:
        print(f"index: {index_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
