from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


EVENT_LOG = Path("data") / "feedback" / "events.jsonl"


def load_feedback_config(path: str | Path = "config/feedback.yaml") -> dict[str, Any]:
    config_path = Path(path)
    if not config_path.exists():
        return {}
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def event_log_path() -> Path:
    config = load_feedback_config().get("feedback") or {}
    return Path(config.get("event_log") or EVENT_LOG)


def append_event(event: dict[str, Any]) -> Path:
    path = event_log_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "weight": 1.0,
        "note": "",
        **{key: value for key, value in event.items() if value is not None},
    }
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
    return path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Record local feedback for AI Research Radar.")
    sub = parser.add_subparsers(dest="command", required=True)

    rate = sub.add_parser("rate", help="Rate an item.")
    rate.add_argument("item_id")
    rate.add_argument("event", choices=[
        "relevant",
        "highly_relevant",
        "irrelevant",
        "not_my_direction",
        "read",
        "deep_read_completed",
        "skimmed",
        "saved",
        "archived",
        "clone_and_run",
        "used_as_baseline",
        "used_in_project",
        "cited",
    ])
    rate.add_argument("--track-id", default=None)
    rate.add_argument("--project-id", default=None)
    rate.add_argument("--weight", type=float, default=1.0)
    rate.add_argument("--note", default="")

    follow_author = sub.add_parser("follow-author", help="Follow an author/scholar.")
    follow_author.add_argument("author_id")
    follow_author.add_argument("--note", default="")

    mute_source = sub.add_parser("mute-source", help="Mute a source id.")
    mute_source.add_argument("source_id")
    mute_source.add_argument("--note", default="")

    mute_topic = sub.add_parser("mute-topic", help="Mute a track/topic id.")
    mute_topic.add_argument("track_id")
    mute_topic.add_argument("--note", default="")

    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "rate":
        path = append_event(
            {
                "item_id": args.item_id,
                "event": args.event,
                "track_id": args.track_id,
                "project_id": args.project_id,
                "weight": args.weight,
                "note": args.note,
            }
        )
    elif args.command == "follow-author":
        path = append_event({"event": "follow_author", "author_id": args.author_id, "note": args.note})
    elif args.command == "mute-source":
        path = append_event({"event": "muted_source", "source_id": args.source_id, "note": args.note})
    elif args.command == "mute-topic":
        path = append_event({"event": "muted_topic", "track_id": args.track_id, "note": args.note})
    else:
        raise SystemExit(f"Unsupported command: {args.command}")
    print(f"Feedback recorded: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
