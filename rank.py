from __future__ import annotations

import argparse
import json
import math
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml
from dateutil import parser as date_parser


SOURCE_CREDIBILITY = {
    "primary": 0.88,
    "aggregator": 0.72,
    "media": 0.62,
}

OFFICIAL_HINTS = [
    "arxiv.org",
    "openreview.net",
    "openai.com",
    "anthropic.com",
    "deepmind.google",
    "research.google",
    "meta.com",
    "microsoft.com",
    "nvidia.com",
    "apple.com",
    "stanford.edu",
    "mit.edu",
    "berkeley.edu",
    "cmu.edu",
    "princeton",
    "neurips.cc",
    "icml.cc",
    "iclr.cc",
    "aclweb.org",
    "thecvf.com",
    "ecva.net",
    "roboticsconference.org",
    "corl.org",
]


def load_yaml(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_json(path: str | Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: str | Path, payload: Any) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def normalize_title(title: str) -> str:
    text = title.lower()
    text = re.sub(r"\barxiv\s*:\s*", "", text)
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def arxiv_id(url: str) -> str | None:
    match = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", url)
    return match.group(1) if match else None


def canonical_key(item: dict[str, Any]) -> str:
    url = item.get("url", "")
    parsed = urlparse(url)
    aid = arxiv_id(url)
    if aid:
        return f"arxiv:{aid}"
    if "openreview.net" in parsed.netloc:
        forum = re.search(r"id=([A-Za-z0-9_-]+)", url)
        if forum:
            return f"openreview:{forum.group(1)}"
    title = normalize_title(item.get("title", ""))
    return f"title:{title[:160]}"


def source_priority(kind: str) -> int:
    return {"primary": 3, "aggregator": 2, "media": 1}.get(kind, 0)


def dedupe_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    buckets: dict[str, dict[str, Any]] = {}
    for item in items:
        key = canonical_key(item)
        existing = buckets.get(key)
        if not existing:
            item["duplicate_sources"] = [item.get("source", {})]
            buckets[key] = item
            continue

        existing["duplicate_sources"].append(item.get("source", {}))
        existing_kind = existing.get("source", {}).get("kind", "primary")
        new_kind = item.get("source", {}).get("kind", "primary")
        better_source = source_priority(new_kind) > source_priority(existing_kind)
        better_summary = len(item.get("summary", "")) > len(existing.get("summary", ""))
        if better_source or (new_kind == existing_kind and better_summary):
            merged_sources = existing["duplicate_sources"]
            item["duplicate_sources"] = merged_sources
            buckets[key] = item
    return list(buckets.values())


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = date_parser.parse(value)
    except (TypeError, ValueError, OverflowError):
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def keyword_score(item: dict[str, Any], keywords: dict[str, Any]) -> tuple[float, list[str], list[str]]:
    text = " ".join(
        [
            item.get("title", ""),
            item.get("summary", ""),
            " ".join(item.get("tags", [])),
        ]
    ).lower()

    matched_terms: list[str] = []
    matched_areas: list[str] = []
    score = 0.0
    for area in keywords.get("focus_areas", []):
        area_hits = 0
        for term in area.get("terms", []):
            term_lower = str(term).lower()
            if term_matches(term_lower, text):
                area_hits += 1
                matched_terms.append(term)
        if area_hits:
            matched_areas.append(area.get("name", "Unknown"))
            score += float(area.get("weight", 1.0)) * (1.0 + math.log1p(area_hits))

    for term in keywords.get("boost_terms", []):
        if term_matches(str(term).lower(), text):
            score += 0.25
            matched_terms.append(term)

    for term in keywords.get("negative_terms", []):
        if term_matches(str(term).lower(), text):
            score -= 0.45

    normalized = max(0.0, min(1.0, score / 4.5))
    return normalized, sorted(set(matched_terms)), sorted(set(matched_areas))


def term_matches(term: str, text: str) -> bool:
    if not term:
        return False
    if re.fullmatch(r"[a-z0-9+#.-]+", term):
        return re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", text) is not None
    return term in text


def credibility_score(item: dict[str, Any]) -> float:
    source = item.get("source", {})
    kind = source.get("kind", "primary")
    score = SOURCE_CREDIBILITY.get(kind, 0.65)
    url = (item.get("url") or "") + " " + (source.get("url") or "")
    if any(hint in url for hint in OFFICIAL_HINTS):
        score += 0.07
    if item.get("duplicate_sources") and len(item["duplicate_sources"]) > 1:
        score += min(0.08, 0.02 * (len(item["duplicate_sources"]) - 1))
    return max(0.0, min(1.0, score))


def novelty_score(item: dict[str, Any], now: datetime | None = None) -> float:
    now = now or datetime.now(timezone.utc)
    published = parse_date(item.get("published_at"))
    if not published:
        base = 0.55
    else:
        age_days = max(0.0, (now - published).total_seconds() / 86400)
        if age_days <= 1:
            base = 1.0
        elif age_days <= 3:
            base = 0.86
        elif age_days <= 7:
            base = 0.68
        elif age_days <= 30:
            base = 0.45
        else:
            base = 0.22
    metrics = item.get("metrics", {})
    upvotes = metrics.get("upvotes")
    if isinstance(upvotes, (int, float)) and upvotes > 0:
        base += min(0.12, math.log1p(upvotes) / 50)
    return max(0.0, min(1.0, base))


def actionability_score(item: dict[str, Any], matched_terms: list[str]) -> float:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    score = 0.35
    actionable_terms = [
        "code",
        "github",
        "dataset",
        "benchmark",
        "leaderboard",
        "evaluation",
        "release",
        "open-source",
        "open source",
        "framework",
        "library",
        "inference",
        "serving",
        "distillation",
        "agent",
    ]
    score += min(0.35, 0.05 * sum(1 for term in actionable_terms if term_matches(term, text)))
    score += min(0.20, 0.03 * len(matched_terms))
    if item.get("source", {}).get("kind") == "media":
        score -= 0.05
    return max(0.0, min(1.0, score))


def score_item(item: dict[str, Any], keywords: dict[str, Any]) -> dict[str, Any]:
    relevance, matched_terms, matched_areas = keyword_score(item, keywords)
    credibility = credibility_score(item)
    novelty = novelty_score(item)
    actionability = actionability_score(item, matched_terms)
    overall = (
        relevance * 0.40
        + credibility * 0.25
        + novelty * 0.20
        + actionability * 0.15
    )
    item["scores"] = {
        "relevance": round(relevance, 3),
        "credibility": round(credibility, 3),
        "novelty": round(novelty, 3),
        "actionability": round(actionability, 3),
        "overall": round(overall, 3),
    }
    item["matched_keywords"] = matched_terms
    item["matched_focus_areas"] = matched_areas
    item["worth_deep_read"] = bool(overall >= 0.62 and relevance >= 0.22 and credibility >= 0.62)
    return item


def rank_items(
    items: list[dict[str, Any]],
    keywords_path: str | Path = "keywords.yaml",
    limit: int | None = None,
) -> list[dict[str, Any]]:
    keywords = load_yaml(keywords_path)
    deduped = dedupe_items(items)
    scored = [score_item(item, keywords) for item in deduped]
    scored.sort(key=lambda item: item.get("scores", {}).get("overall", 0), reverse=True)
    return scored[:limit] if limit else scored


def main() -> int:
    parser = argparse.ArgumentParser(description="Deduplicate and rank fetched items.")
    parser.add_argument("--input", default="data/raw.json")
    parser.add_argument("--output", default="data/ranked.json")
    parser.add_argument("--keywords", default="keywords.yaml")
    parser.add_argument("--limit", type=int, default=80)
    args = parser.parse_args()

    ranked = rank_items(load_json(args.input), args.keywords, args.limit)
    save_json(args.output, ranked)
    print(f"wrote {len(ranked)} ranked items to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
