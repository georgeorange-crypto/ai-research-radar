from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from fetch import configure_logging, fetch_all, save_json
from rank import rank_items
from summarize import generate_report


def today(tz_name: str) -> str:
    return datetime.now(ZoneInfo(tz_name)).strftime("%Y-%m-%d")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the AI research radar pipeline.")
    parser.add_argument("--date", default=None)
    parser.add_argument("--timezone", default=os.getenv("RADAR_TIMEZONE", "Asia/Shanghai"))
    parser.add_argument("--sources", default="sources.yaml")
    parser.add_argument("--keywords", default="keywords.yaml")
    parser.add_argument("--rank-limit", type=int, default=int(os.getenv("RADAR_RANK_LIMIT", "100")))
    parser.add_argument("--max-report-items", type=int, default=int(os.getenv("RADAR_MAX_REPORT_ITEMS", "35")))
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    configure_logging(args.verbose)
    report_date = args.date or today(args.timezone)
    Path("data").mkdir(exist_ok=True)
    Path("reports").mkdir(exist_ok=True)

    raw_path = Path("data") / f"raw-{report_date}.json"
    ranked_path = Path("data") / f"ranked-{report_date}.json"
    report_path = Path("reports") / f"{report_date}.md"

    raw_items = fetch_all(args.sources)
    save_json(raw_path, raw_items)
    ranked_items = rank_items(raw_items, args.keywords, args.rank_limit)
    save_json(ranked_path, ranked_items)
    generate_report(
        ranked_items,
        report_path,
        report_date=report_date,
        max_items=args.max_report_items,
        latest_path="report.md",
    )

    print(f"raw items: {len(raw_items)}")
    print(f"ranked items: {len(ranked_items)}")
    print(f"report: {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
