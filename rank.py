from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, unquote, urlparse

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
    "github.com",
]

MUST_READ_LIMIT = 3
SKIM_LIMIT = 8


def clamp_score(value: float) -> float:
    return max(0.0, min(1.0, value))


def load_yaml(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_radar_config(keywords_path: str | Path) -> dict[str, Any]:
    path = Path(keywords_path)
    config = load_yaml(path)
    for sibling in ["scoring.yaml", "classics.yaml"]:
        sibling_path = path.parent / sibling
        if not sibling_path.exists():
            continue
        supplemental = load_yaml(sibling_path)
        for key, value in supplemental.items():
            if key == "classification" and isinstance(value, dict):
                merged = {**value, **(config.get("classification") or {})}
                config["classification"] = merged
            elif key not in config:
                config[key] = value
    return config


def load_json(path: str | Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_jsonl(path: str | Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def save_json(path: str | Path, payload: Any) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def normalize_title(title: str) -> str:
    text = title.lower()
    text = re.sub(r"\barxiv\s*:\s*", "", text)
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


ARXIV_ID_RE = re.compile(r"(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
OPENREVIEW_URL_RE = re.compile(r"openreview\.net/(?:forum|pdf)\?id=([A-Za-z0-9_-]{5,})", re.IGNORECASE)
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)


def metric_value(item: dict[str, Any], *keys: str) -> Any:
    metrics = item.get("metrics") or {}
    if not isinstance(metrics, dict):
        return None
    lowered = {str(key).lower(): value for key, value in metrics.items()}
    for key in keys:
        value = lowered.get(key.lower())
        if value:
            return value
    return None


def normalize_arxiv_id(value: Any) -> str | None:
    if not value:
        return None
    match = ARXIV_ID_RE.search(str(value))
    return match.group(1) if match else None


def arxiv_id(url: str) -> str | None:
    return normalize_arxiv_id(unquote(url or ""))


def extract_arxiv_id(item: dict[str, Any]) -> str | None:
    metric_id = metric_value(item, "arxiv_id", "arxiv", "paper_id")
    return normalize_arxiv_id(metric_id) or arxiv_id(item.get("url", ""))


def normalize_openreview_forum_id(value: Any) -> str | None:
    if not value:
        return None
    forum_id = str(value).strip()
    return forum_id if re.fullmatch(r"[A-Za-z0-9_-]{5,}", forum_id) else None


def openreview_forum_id_from_url(url: str) -> str | None:
    parsed = urlparse(url or "")
    if "openreview.net" not in parsed.netloc.lower():
        return None
    for value in parse_qs(parsed.query).get("id", []):
        forum_id = normalize_openreview_forum_id(value)
        if forum_id:
            return forum_id
    match = OPENREVIEW_URL_RE.search(url or "")
    return normalize_openreview_forum_id(match.group(1)) if match else None


def is_openreview_entry(item: dict[str, Any]) -> bool:
    url = item.get("url", "")
    source = item.get("source", {})
    tags = {str(tag).lower() for tag in item.get("tags", [])}
    return (
        "openreview.net" in urlparse(url).netloc.lower()
        or source.get("type") == "openreview"
        or "openreview" in str(source.get("id", "")).lower()
        or "openreview" in tags
    )


def openreview_forum_url(forum_id: str) -> str:
    return f"https://openreview.net/forum?id={forum_id}"


def extract_openreview_forum_id(item: dict[str, Any]) -> str | None:
    metric_id = metric_value(item, "openreview_forum_id", "forum_id", "note_id", "openreview_id")
    forum_id = normalize_openreview_forum_id(metric_id)
    if forum_id:
        return forum_id

    forum_id = openreview_forum_id_from_url(item.get("url", ""))
    if forum_id:
        return forum_id

    if is_openreview_entry(item):
        text = " ".join([item.get("title", ""), item.get("summary", "")])
        match = OPENREVIEW_URL_RE.search(text)
        if match:
            return normalize_openreview_forum_id(match.group(1))
    return None


def normalize_doi(value: Any) -> str | None:
    if not value:
        return None
    match = DOI_RE.search(unquote(str(value)))
    if not match:
        return None
    return match.group(0).rstrip(".,;:").lower()


def extract_doi(item: dict[str, Any]) -> str | None:
    metric_doi = metric_value(item, "doi")
    return normalize_doi(metric_doi) or normalize_doi(item.get("url", ""))


def ensure_metrics(item: dict[str, Any]) -> dict[str, Any]:
    metrics = item.get("metrics")
    if not isinstance(metrics, dict):
        metrics = {}
        item["metrics"] = metrics
    return metrics


def enrich_item_identifiers(item: dict[str, Any]) -> None:
    metrics = ensure_metrics(item)
    aid = extract_arxiv_id(item)
    if aid and not metrics.get("arxiv_id"):
        metrics["arxiv_id"] = aid

    forum_id = extract_openreview_forum_id(item)
    if forum_id:
        if not metrics.get("openreview_forum_id"):
            metrics["openreview_forum_id"] = forum_id
        if "openreview.net" in urlparse(item.get("url", "")).netloc.lower() or is_openreview_entry(item):
            item["url"] = openreview_forum_url(forum_id)

    doi = extract_doi(item)
    if doi and not metrics.get("doi"):
        metrics["doi"] = doi


def canonical_keys(item: dict[str, Any]) -> list[str]:
    enrich_item_identifiers(item)
    keys: list[str] = []
    aid = extract_arxiv_id(item)
    if aid:
        keys.append(f"arxiv:{aid}")
    forum_id = extract_openreview_forum_id(item)
    if forum_id:
        keys.append(f"openreview:{forum_id}")
    doi = extract_doi(item)
    if doi:
        keys.append(f"doi:{doi}")
    parsed = urlparse(item.get("url", ""))
    if "github.com" in parsed.netloc.lower():
        path = parsed.path.strip("/").lower()
        if path.count("/") >= 1:
            owner, repo, *_ = path.split("/")
            keys.append(f"github:{owner}/{repo}")
    title = normalize_title(item.get("title", ""))
    if title:
        keys.append(f"title:{title[:160]}")
    return keys


def canonical_key(item: dict[str, Any]) -> str:
    keys = canonical_keys(item)
    if keys:
        return keys[0]
    url = item.get("url", "")
    parsed = urlparse(url)
    if "github.com" in parsed.netloc.lower():
        path = parsed.path.strip("/").lower()
        if path.count("/") >= 1:
            owner, repo, *_ = path.split("/")
            return f"github:{owner}/{repo}"
    return f"url:{url.lower()}"


def source_priority(kind: str) -> int:
    return {"primary": 3, "aggregator": 2, "media": 1}.get(kind, 0)


def link_quality(item: dict[str, Any]) -> str:
    if not item.get("url"):
        return "low"
    if is_openreview_entry(item) and not extract_openreview_forum_id(item):
        return "low"
    return "high"


def link_quality_rank(item: dict[str, Any]) -> int:
    return {"low": 0, "high": 1}.get(link_quality(item), 0)


def duplicate_sources(item: dict[str, Any]) -> list[dict[str, Any]]:
    sources = item.get("duplicate_sources")
    if isinstance(sources, list) and sources:
        return [source for source in sources if isinstance(source, dict)]
    source = item.get("source", {})
    return [source] if isinstance(source, dict) else []


def merge_sources(*source_lists: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = []
    seen: set[str] = set()
    for sources in source_lists:
        for source in sources:
            try:
                key = json.dumps(source, ensure_ascii=False, sort_keys=True)
            except TypeError:
                key = str(source)
            if key in seen:
                continue
            seen.add(key)
            merged.append(source)
    return merged


def prefer_item(existing: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    existing_kind = existing.get("source", {}).get("kind", "primary")
    candidate_kind = candidate.get("source", {}).get("kind", "primary")
    better_link = link_quality_rank(candidate) > link_quality_rank(existing)
    same_link = link_quality_rank(candidate) == link_quality_rank(existing)
    better_source = source_priority(candidate_kind) > source_priority(existing_kind)
    better_summary = len(candidate.get("summary", "")) > len(existing.get("summary", ""))
    if better_link or (same_link and (better_source or (candidate_kind == existing_kind and better_summary))):
        return candidate
    return existing


def merge_identifier_metrics(target: dict[str, Any], *items: dict[str, Any]) -> None:
    target_metrics = ensure_metrics(target)
    for item in items:
        metrics = item.get("metrics") or {}
        if not isinstance(metrics, dict):
            continue
        for key in ["arxiv_id", "openreview_forum_id", "doi", "venue_id"]:
            if metrics.get(key) and not target_metrics.get(key):
                target_metrics[key] = metrics[key]
    enrich_item_identifiers(target)


def merge_duplicate_items(existing: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    enrich_item_identifiers(existing)
    enrich_item_identifiers(candidate)
    preferred = prefer_item(existing, candidate)
    preferred["duplicate_sources"] = merge_sources(duplicate_sources(existing), duplicate_sources(candidate))
    merge_identifier_metrics(preferred, existing, candidate)
    return preferred


def dedupe_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    buckets: dict[int, dict[str, Any]] = {}
    bucket_keys: dict[int, set[str]] = {}
    key_to_bucket: dict[str, int] = {}
    next_bucket = 0

    for item in items:
        keys = canonical_keys(item)
        matching_buckets = sorted({key_to_bucket[key] for key in keys if key in key_to_bucket})
        if not matching_buckets:
            item["duplicate_sources"] = [item.get("source", {})]
            buckets[next_bucket] = item
            bucket_keys[next_bucket] = set(keys)
            for key in keys:
                key_to_bucket[key] = next_bucket
            next_bucket += 1
            continue

        primary_bucket = matching_buckets[0]
        for bucket in matching_buckets[1:]:
            buckets[primary_bucket] = merge_duplicate_items(buckets[primary_bucket], buckets[bucket])
            bucket_keys[primary_bucket].update(bucket_keys[bucket])
            for key in bucket_keys[bucket]:
                key_to_bucket[key] = primary_bucket
            del buckets[bucket]
            del bucket_keys[bucket]

        buckets[primary_bucket] = merge_duplicate_items(buckets[primary_bucket], item)
        bucket_keys[primary_bucket].update(keys)
        for key in bucket_keys[primary_bucket]:
            key_to_bucket[key] = primary_bucket
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


def term_matches(term: str, text: str) -> bool:
    if not term:
        return False
    if re.fullmatch(r"[a-z0-9+#.-]+", term):
        return re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", text) is not None
    return term in text


def item_text(item: dict[str, Any]) -> str:
    return " ".join(
        [
            item.get("title", ""),
            item.get("summary", ""),
            " ".join(str(tag) for tag in item.get("tags", [])),
            item.get("source", {}).get("name", ""),
        ]
    ).lower()


def section_configs(config: dict[str, Any]) -> list[dict[str, Any]]:
    sections = config.get("sections")
    if sections:
        return sorted(sections, key=lambda section: int(section.get("order", 999)))

    # Backward-compatible fallback for older keyword files.
    fallback = []
    for idx, area in enumerate(config.get("focus_areas", []), 1):
        fallback.append(
            {
                "id": re.sub(r"[^a-z0-9]+", "_", str(area.get("name", f"section_{idx}")).lower()).strip("_"),
                "title": area.get("name", f"Section {idx}"),
                "group": "core_focus",
                "order": idx * 10,
                "weight": area.get("weight", 1.0),
                "terms": area.get("terms", []),
            }
        )
    return fallback


def score_section(item: dict[str, Any], section: dict[str, Any], text: str) -> tuple[float, list[str]]:
    hits: list[str] = []
    raw = 0.0
    for term in section.get("terms", []):
        term_lower = str(term).lower()
        if term_matches(term_lower, text):
            hits.append(str(term))
            raw += 1.0

    item_tags = {str(tag) for tag in item.get("tags", [])}
    for category in section.get("categories", []) or []:
        if category in item_tags:
            raw += 1.25
            hits.append(category)

    source_text = " ".join(
        [
            item.get("source", {}).get("name", ""),
            item.get("source", {}).get("id", ""),
            item.get("url", ""),
        ]
    ).lower()
    for hint in section.get("source_hints", []) or []:
        if str(hint).lower() in source_text:
            raw += 0.5
            hits.append(str(hint))

    if raw <= 0:
        return 0.0, []

    weighted = float(section.get("weight", 1.0)) * (1.0 + math.log1p(raw))
    return weighted, sorted(set(hits))


def classification_settings(config: dict[str, Any]) -> dict[str, Any]:
    settings = config.get("classification") or {}
    return settings if isinstance(settings, dict) else {}


def resolve_fallback_section(config: dict[str, Any], by_id: dict[str, dict[str, Any]]) -> str:
    configured = str(classification_settings(config).get("fallback_section", "")).strip()
    for section_id in [configured, "highlights", "other_highlights"]:
        if section_id and section_id in by_id:
            return section_id
    return next(iter(by_id), "other_highlights")


def classify_item(
    item: dict[str, Any],
    config: dict[str, Any],
) -> tuple[str, str, str, dict[str, float], list[str], list[str], list[dict[str, Any]]]:
    text = item_text(item)
    scores: dict[str, float] = {}
    hits_by_section: dict[str, list[str]] = {}
    sections = section_configs(config)
    by_id = {section["id"]: section for section in sections}
    settings = classification_settings(config)

    for section in sections:
        score, hits = score_section(item, section, text)
        scores[section["id"]] = score
        if hits:
            hits_by_section[section["id"]] = hits

    if scores:
        primary_id = max(scores, key=scores.get)
        primary_score = scores[primary_id]
    else:
        primary_id = resolve_fallback_section(config, by_id)
        primary_score = 0.0

    fallback_id = resolve_fallback_section(config, by_id)
    fallback_min_score = float(settings.get("fallback_min_score", 0.45))
    if primary_score < fallback_min_score and fallback_id in by_id:
        other_score, other_hits = score_section(item, by_id[fallback_id], text)
        if other_score > 0:
            primary_id = fallback_id
            primary_score = other_score
            hits_by_section[primary_id] = other_hits

    primary = by_id.get(primary_id, {"title": "Other Highlights", "group": "other"})
    matched_terms = sorted({term for terms in hits_by_section.values() for term in terms})
    score_divisor = float(settings.get("normalized_score_divisor", 4.0))
    normalized_scores = {
        key: round(min(1.0, value / score_divisor), 3)
        for key, value in scores.items()
        if value > 0
    }

    min_section_score = float(settings.get("min_section_score", 0.0))
    max_labels = int(settings.get("max_labels_per_item", 5))
    matched_section_entries = []
    for section_id, score in sorted(scores.items(), key=lambda pair: pair[1], reverse=True):
        if score <= min_section_score or section_id not in by_id:
            continue
        section = by_id[section_id]
        matched_section_entries.append(
            {
                "id": section_id,
                "title": section.get("title", section_id),
                "group": section.get("group", "other"),
                "score": normalized_scores.get(section_id, 0),
                "matched_terms": hits_by_section.get(section_id, []),
            }
        )
        if len(matched_section_entries) >= max_labels:
            break
    matched_sections = [section["title"] for section in matched_section_entries]
    return (
        primary_id,
        primary.get("title", primary_id),
        primary.get("group", "other"),
        normalized_scores,
        matched_terms,
        matched_sections,
        matched_section_entries,
    )


def boost_matches(item: dict[str, Any], config: dict[str, Any]) -> list[str]:
    text = item_text(item)
    return sorted({str(term) for term in config.get("boost_terms", []) if term_matches(str(term).lower(), text)})


def relevance_score(section_scores: dict[str, float], matched_terms: list[str], section_group: str) -> float:
    base = max(section_scores.values(), default=0.0)
    term_bonus = min(0.18, 0.018 * len(matched_terms))
    group_bonus = 0.06 if section_group in {"core_focus", "primary_research"} else 0.0
    return max(0.0, min(1.0, base + term_bonus + group_bonus))


def score_rank_key(item: dict[str, Any]) -> tuple[float, float, float]:
    scores = item.get("scores", {})
    return (
        scores.get("personal_score", 0.0),
        scores.get("global_score", 0.0),
        scores.get("research_relevance", 0.0),
    )


def credibility_score(item: dict[str, Any], config: dict[str, Any]) -> float:
    source = item.get("source", {})
    kind = source.get("kind", "primary")
    source_credibility = config.get("source_credibility", SOURCE_CREDIBILITY)
    score = source_credibility.get(kind, 0.65)
    url = (item.get("url") or "") + " " + (source.get("url") or "")
    if any(hint in url for hint in config.get("official_hints", OFFICIAL_HINTS)):
        score += 0.07
    if item.get("duplicate_sources") and len(item["duplicate_sources"]) > 1:
        score += min(0.08, 0.02 * (len(item["duplicate_sources"]) - 1))
    if source.get("type") == "github_search":
        stars = item.get("metrics", {}).get("stars", 0) or 0
        score += min(0.10, math.log1p(stars) / 80)
    return clamp_score(score)


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
        elif age_days <= 180:
            base = 0.28
        else:
            base = 0.16
    metrics = item.get("metrics", {})
    upvotes = metrics.get("upvotes")
    if isinstance(upvotes, (int, float)) and upvotes > 0:
        base += min(0.12, math.log1p(upvotes) / 50)
    return max(0.0, min(1.0, base))


def community_signal_score(item: dict[str, Any]) -> float:
    metrics = item.get("metrics", {})
    score = 0.08
    upvotes = metrics.get("upvotes")
    if isinstance(upvotes, (int, float)) and upvotes > 0:
        score += min(0.28, math.log1p(upvotes) / 18)
    stars = metrics.get("stars")
    if isinstance(stars, (int, float)) and stars > 0:
        score += min(0.50, math.log1p(stars) / 14)
    forks = metrics.get("forks")
    if isinstance(forks, (int, float)) and forks > 0:
        score += min(0.12, math.log1p(forks) / 25)
    if item.get("duplicate_sources") and len(item["duplicate_sources"]) > 1:
        score += min(0.15, 0.04 * (len(item["duplicate_sources"]) - 1))
    if item.get("source", {}).get("type") == "github_search":
        score += 0.08
    return clamp_score(score)


def evidence_strength_score(item: dict[str, Any], config: dict[str, Any]) -> float:
    source = item.get("source", {})
    kind = source.get("kind", "primary")
    score = {"primary": 0.72, "aggregator": 0.52, "media": 0.42}.get(kind, 0.50)
    url = (item.get("url") or "") + " " + (source.get("url") or "")
    if any(hint in url for hint in config.get("official_hints", OFFICIAL_HINTS)):
        score += 0.08
    summary_len = len(item.get("summary", "") or "")
    if summary_len >= 500:
        score += 0.10
    elif summary_len >= 160:
        score += 0.06
    elif summary_len == 0:
        score -= 0.08
    if item.get("authors"):
        score += 0.04
    if item.get("tags"):
        score += 0.03
    if item.get("duplicate_sources") and len(item["duplicate_sources"]) > 1:
        score += min(0.08, 0.03 * (len(item["duplicate_sources"]) - 1))
    if source.get("type") == "github_search":
        score -= 0.08
    return clamp_score(score)


def actionability_score(item: dict[str, Any], matched_terms: list[str], config: dict[str, Any]) -> float:
    text = item_text(item)
    score = 0.30
    actionable_terms = config.get(
        "actionable_terms",
        [
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
            "tool",
        ],
    )
    score += min(0.34, 0.045 * sum(1 for term in actionable_terms if term_matches(term, text)))
    score += min(0.18, 0.025 * len(matched_terms))
    if item.get("source", {}).get("type") == "github_search":
        stars = item.get("metrics", {}).get("stars", 0) or 0
        score += 0.20 + min(0.12, math.log1p(stars) / 65)
    if item.get("source", {}).get("kind") == "media":
        score -= 0.05
    return clamp_score(score)


def is_negative(item: dict[str, Any], config: dict[str, Any]) -> bool:
    text = item_text(item)
    return any(term_matches(str(term).lower(), text) for term in config.get("negative_terms", []))


def is_open_source_project(item: dict[str, Any]) -> bool:
    text = item_text(item)
    url = item.get("url", "")
    source_type = item.get("source", {}).get("type")
    return (
        source_type == "github_search"
        or "github.com" in urlparse(url).netloc
        or term_matches("github", text)
        or term_matches("open-source", text)
        or term_matches("open source", text)
        or term_matches("code release", text)
    )


def composite_scores(
    *,
    research_relevance: float,
    novelty: float,
    credibility: float,
    evidence_strength: float,
    community_signal: float,
    actionability: float,
    section_group: str,
    negative: bool,
) -> tuple[float, float]:
    global_score = (
        research_relevance * 0.12
        + novelty * 0.24
        + credibility * 0.18
        + evidence_strength * 0.18
        + community_signal * 0.14
        + actionability * 0.14
    )
    personal_score = (
        research_relevance * 0.42
        + novelty * 0.14
        + credibility * 0.12
        + evidence_strength * 0.08
        + community_signal * 0.06
        + actionability * 0.18
    )
    if section_group in {"core_focus", "primary_research"}:
        personal_score += 0.05
    elif section_group == "other":
        personal_score -= 0.02
    if negative:
        global_score -= 0.15
        personal_score -= 0.25
    return clamp_score(global_score), clamp_score(personal_score)


def score_item(item: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    enrich_item_identifiers(item)
    item_link_quality = link_quality(item)
    (
        section_id,
        section_title,
        section_group,
        section_scores,
        section_terms,
        matched_sections,
        matched_section_entries,
    ) = classify_item(item, config)
    boosts = boost_matches(item, config)
    matched_terms = sorted(set(section_terms + boosts))
    research_relevance = relevance_score(section_scores, section_terms, section_group)
    credibility = credibility_score(item, config)
    novelty = novelty_score(item)
    evidence_strength = evidence_strength_score(item, config)
    community_signal = community_signal_score(item)
    actionability = actionability_score(item, matched_terms, config)
    if item_link_quality == "low":
        credibility = clamp_score(credibility - 0.25)
        actionability = clamp_score(actionability - 0.20)
    negative = is_negative(item, config)
    global_score, personal_score = composite_scores(
        research_relevance=research_relevance,
        novelty=novelty,
        credibility=credibility,
        evidence_strength=evidence_strength,
        community_signal=community_signal,
        actionability=actionability,
        section_group=section_group,
        negative=negative,
    )

    item["primary_section"] = {
        "id": section_id,
        "title": section_title,
        "group": section_group,
    }
    item["section_scores"] = section_scores
    item["matched_sections"] = matched_section_entries
    item["matched_keywords"] = matched_terms
    item["matched_focus_areas"] = matched_sections
    item["is_open_source_project"] = is_open_source_project(item)
    item["link_quality"] = item_link_quality
    item["quality_flags"] = {
        "negative_terms": negative,
        "missing_url": not bool(item.get("url")),
        "low_quality_link": item_link_quality == "low",
        "missing_openreview_forum_id": is_openreview_entry(item) and not extract_openreview_forum_id(item),
    }
    item["scores"] = {
        "global_score": round(global_score, 3),
        "personal_score": round(personal_score, 3),
        "novelty": round(novelty, 3),
        "credibility": round(credibility, 3),
        "evidence_strength": round(evidence_strength, 3),
        "community_signal": round(community_signal, 3),
        "actionability": round(actionability, 3),
        "research_relevance": round(research_relevance, 3),
    }
    return item


def tier_reason(item: dict[str, Any], tier: str) -> str:
    scores = item.get("scores", {})
    if tier == "MUST_READ":
        return "personal_score 达到深读阈值，且进入当日 MUST_READ 名额。"
    if tier == "SKIM":
        return "personal_score 或 global_score 达到略读阈值，适合快速判断价值。"
    if tier == "ARCHIVE":
        return "有研究或情报价值，但未进入当日深读/略读名额。"
    if item.get("quality_flags", {}).get("missing_url"):
        return "缺少可打开原文链接。"
    if item.get("quality_flags", {}).get("negative_terms"):
        return "命中营销、招聘、活动注册等低价值信号。"
    if scores.get("research_relevance", 0) < 0.10:
        return "与 AI 研究固定版块相关性较弱。"
    return "质量、证据或相关性不足以进入跟踪队列。"


def ignore_reason(item: dict[str, Any]) -> str | None:
    scores = item.get("scores", {})
    if not item.get("url"):
        return "缺少可打开原文链接。"
    if item.get("quality_flags", {}).get("negative_terms"):
        return "命中营销、招聘、活动注册等低价值信号。"
    if scores.get("credibility", 0) < 0.40 and scores.get("evidence_strength", 0) < 0.35:
        return "来源可信度和证据强度都偏低。"
    if (
        scores.get("research_relevance", 0) < 0.10
        and scores.get("actionability", 0) < 0.55
        and scores.get("global_score", 0) < 0.70
    ):
        return "与 AI 研究弱相关，且缺少明显可操作或全局重要性信号。"
    return None


def archive_worthy(item: dict[str, Any]) -> bool:
    scores = item.get("scores", {})
    return (
        scores.get("personal_score", 0) >= 0.45
        or scores.get("global_score", 0) >= 0.55
        or scores.get("research_relevance", 0) >= 0.18
        or scores.get("actionability", 0) >= 0.55
        or (scores.get("credibility", 0) >= 0.80 and scores.get("novelty", 0) >= 0.45)
    )


def assign_reading_tiers(items: list[dict[str, Any]]) -> None:
    ranked = sorted(items, key=score_rank_key, reverse=True)
    must_count = 0
    skim_count = 0

    for item in ranked:
        scores = item.get("scores", {})
        reason = ignore_reason(item)
        if reason:
            tier = "IGNORE"
            item["reading_tier_reason"] = reason
            item["reading_tier"] = tier
            item["worth_deep_read"] = False
            continue

        if scores.get("personal_score", 0) >= 0.86 and must_count < MUST_READ_LIMIT:
            tier = "MUST_READ"
            must_count += 1
        elif (
            (scores.get("personal_score", 0) >= 0.72 or scores.get("global_score", 0) >= 0.85)
            and skim_count < SKIM_LIMIT
        ):
            tier = "SKIM"
            skim_count += 1
        elif archive_worthy(item):
            tier = "ARCHIVE"
        else:
            tier = "IGNORE"

        item["reading_tier"] = tier
        item["reading_tier_reason"] = tier_reason(item, tier)
        item["worth_deep_read"] = tier == "MUST_READ"


def section_catalog(config: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "id": section["id"],
            "title": section.get("title", section["id"]),
            "group": section.get("group", "other"),
            "order": int(section.get("order", 999)),
        }
        for section in section_configs(config)
    ]


def item_section_ids(item: dict[str, Any]) -> set[str]:
    section_ids = {
        str(section.get("id"))
        for section in item.get("matched_sections", [])
        if section.get("id")
    }
    primary_id = item.get("primary_section", {}).get("id")
    if primary_id:
        section_ids.add(str(primary_id))
    return section_ids


def build_section_payloads(items: list[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    sections = []
    for section in section_catalog(config):
        section_items = [
            item
            for item in items
            if item.get("reading_tier") != "IGNORE"
            and section["id"] in item_section_ids(item)
            and item.get("source", {}).get("type") != "github_search"
        ]
        section_items.sort(key=score_rank_key, reverse=True)
        sections.append({**section, "items": section_items})
    return sections


def select_github_projects(items: list[dict[str, Any]], limit: int = 5) -> list[dict[str, Any]]:
    projects = [item for item in items if item.get("reading_tier") != "IGNORE" and item.get("is_open_source_project")]
    projects.sort(
        key=lambda item: (
            item.get("source", {}).get("type") == "github_search",
            item.get("scores", {}).get("actionability", 0),
            item.get("scores", {}).get("community_signal", 0),
            item.get("metrics", {}).get("stars", 0) or 0,
            item.get("scores", {}).get("personal_score", 0),
        ),
        reverse=True,
    )
    return projects[:limit]


CLASSIC_TOPIC_ALIASES = {
    "context_memory": "context_compression",
    "context_compression": "context_compression",
    "long_context": "context_compression",
    "agents": "agents",
    "planning": "agents",
    "tool_use": "agents",
    "open_world": "open_world_learning",
    "open_world_learning": "open_world_learning",
    "open_set_recognition": "open_world_learning",
    "continual_learning": "open_world_learning",
    "distillation_efficiency": "model_distillation",
    "model_distillation": "model_distillation",
    "model_compression": "model_distillation",
    "efficient_training": "model_distillation",
    "architecture": "model_architecture",
    "model_architecture": "model_architecture",
    "rl": "rl",
    "cv": "cv",
    "nlp": "nlp",
    "learning_methods": "learning_methods",
    "ai_systems": "highlights",
    "interpretability": "highlights",
    "ai_for_science": "highlights",
    "biology": "highlights",
}

CLASSIC_ROTATION = {
    0: ("Context Compression / Long Context", {"context_compression", "long_context"}),
    1: ("Agents", {"agents", "planning", "tool_use"}),
    2: ("Open-World Learning", {"open_world_learning", "open_set_recognition", "continual_learning"}),
    3: ("Distillation", {"model_distillation", "model_compression", "efficient_training"}),
    4: ("RL", {"rl"}),
    5: ("CV / NLP / Architecture", {"cv", "nlp", "model_architecture"}),
    6: ("AI Systems / Interpretability / AI for Science", {"ai_systems", "interpretability", "ai_for_science", "biology"}),
}


def normalized_topic_tags(paper: dict[str, Any]) -> set[str]:
    tags = {str(tag).strip().lower() for tag in paper.get("topic_tags", []) if str(tag).strip()}
    return {CLASSIC_TOPIC_ALIASES.get(tag, tag) for tag in tags} | tags


def related_modern_keywords(paper: dict[str, Any]) -> set[str]:
    return {str(keyword).strip().lower() for keyword in paper.get("related_modern_keywords", []) if str(keyword).strip()}


def item_keywords(item: dict[str, Any]) -> set[str]:
    return {str(keyword).strip().lower() for keyword in item.get("matched_keywords", []) if str(keyword).strip()}


def classic_connection_terms(paper: dict[str, Any], item: dict[str, Any]) -> list[str]:
    text = item_text(item)
    keyword_hits = [
        keyword
        for keyword in related_modern_keywords(paper)
        if keyword and (keyword in text or keyword in item_keywords(item))
    ]
    section_hits = normalized_topic_tags(paper).intersection(item_section_ids(item))
    return sorted(set(keyword_hits + list(section_hits)))[:8]


def classic_relation_score(paper: dict[str, Any], item: dict[str, Any]) -> tuple[float, list[str]]:
    terms = classic_connection_terms(paper, item)
    if not terms:
        return 0.0, []
    section_bonus = 1.25 * len(normalized_topic_tags(paper).intersection(item_section_ids(item)))
    keyword_bonus = 0.75 * len(set(terms).intersection(related_modern_keywords(paper)))
    item_bonus = item.get("scores", {}).get("personal_score", 0.0)
    return section_bonus + keyword_bonus + item_bonus, terms


def parse_report_date(report_date: str | None) -> datetime:
    if report_date:
        try:
            return datetime.strptime(report_date, "%Y-%m-%d")
        except ValueError:
            pass
    return datetime.now()


def rotation_topic(report_date: str | None) -> tuple[str, set[str]]:
    return CLASSIC_ROTATION[parse_report_date(report_date).weekday()]


def paper_related_sections(paper: dict[str, Any], config: dict[str, Any]) -> list[str]:
    topics = normalized_topic_tags(paper)
    section_names = [
        section.get("title", section["id"])
        for section in section_catalog(config)
        if section["id"] in topics
    ]
    if section_names:
        return section_names
    return [str(tag) for tag in paper.get("topic_tags", [])[:4]]


def build_classic_result(
    paper: dict[str, Any],
    config: dict[str, Any],
    related_items: list[tuple[dict[str, Any], list[str]]],
    connection: str,
) -> dict[str, Any]:
    return {
        **paper,
        "related_sections": paper_related_sections(paper, config),
        "related_today": [
            {
                "title": item.get("title"),
                "url": item.get("url"),
                "section": item.get("primary_section", {}).get("title"),
                "connection_terms": terms,
            }
            for item, terms in related_items[:3]
        ],
        "modern_connection": connection,
        "why_now": paper.get("why_classic", "用于把今天的新结果放回经典脉络中理解。"),
    }


def select_classic_papers(
    items: list[dict[str, Any]],
    config: dict[str, Any],
    limit: int = 2,
    *,
    report_date: str | None = None,
) -> list[dict[str, Any]]:
    papers = config.get("classic_papers", [])
    if not papers:
        return []

    must_read_items = [item for item in items if item.get("reading_tier") == "MUST_READ"]
    selected: list[tuple[float, int, dict[str, Any], list[tuple[dict[str, Any], list[str]]], str]] = []
    for paper in papers:
        related_items: list[tuple[dict[str, Any], list[str]]] = []
        relation_score = 0.0
        for item in must_read_items:
            score, terms = classic_relation_score(paper, item)
            if score <= 0:
                continue
            relation_score += score
            related_items.append((item, terms))
        if relation_score <= 0:
            continue
        terms_text = "、".join(sorted({term for _, terms in related_items for term in terms})[:6])
        connection = f"它和今日 MUST_READ 的连接在于：{terms_text}。这些新条目正在重新触发这篇经典论文中的问题设定或方法假设。"
        selected.append((relation_score, int(paper.get("year", 0)), paper, related_items, connection))

    if not selected:
        rotation_label, rotation_tags = rotation_topic(report_date)
        rotation_topics = {CLASSIC_TOPIC_ALIASES.get(tag, tag) for tag in rotation_tags} | rotation_tags
        for paper in papers:
            topic_overlap = normalized_topic_tags(paper).intersection(rotation_topics)
            if not topic_overlap:
                continue
            connection = (
                f"今天没有足够明确的 MUST_READ 经典连接，因此按星期主题轮换到 {rotation_label}。"
                "它为今日新论文提供背景坐标：哪些问题已经被经典工作定义过，哪些只是换了新的模型和工程约束。"
            )
            selected.append((float(len(topic_overlap)), int(paper.get("year", 0)), paper, [], connection))

    if not selected:
        selected = [
            (
                0.0,
                int(paper.get("year", 0)),
                paper,
                [],
                "今天没有明显主题连接；先选一篇经典论文维持基础脉络复习。",
            )
            for paper in papers[:limit]
        ]

    selected.sort(key=lambda row: (row[0], row[1]), reverse=True)
    return [
        build_classic_result(paper, config, related_items, connection)
        for _, _, paper, related_items, connection in selected[:limit]
    ]


def process_items(
    items: list[dict[str, Any]],
    keywords_path: str | Path = "config/keywords.yaml",
    *,
    report_date: str | None = None,
    limit: int | None = None,
) -> dict[str, Any]:
    config = load_radar_config(keywords_path)
    deduped = dedupe_items(items)
    scored = [score_item(item, config) for item in deduped]
    scored.sort(key=score_rank_key, reverse=True)
    if limit:
        scored = scored[:limit]
    assign_reading_tiers(scored)

    tier_counts = Counter(item.get("reading_tier", "IGNORE") for item in scored)
    sections = build_section_payloads(scored, config)
    github_projects = select_github_projects(scored)
    classic_revisit = select_classic_papers(scored, config, report_date=report_date)

    return {
        "date": report_date or datetime.now().strftime("%Y-%m-%d"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "schema_version": 4,
        "counts": {
            "raw": len(items),
            "deduped": len(deduped),
            "processed": len(scored),
            "must_read": tier_counts.get("MUST_READ", 0),
            "skim": tier_counts.get("SKIM", 0),
            "archive": tier_counts.get("ARCHIVE", 0),
            "ignore": tier_counts.get("IGNORE", 0),
            "github_projects": len(github_projects),
        },
        "tier_limits": {
            "MUST_READ": MUST_READ_LIMIT,
            "SKIM": SKIM_LIMIT,
        },
        "section_catalog": section_catalog(config),
        "sections": sections,
        "github_projects": github_projects,
        "classic_revisit": classic_revisit,
        "items": scored,
    }


def rank_items(
    items: list[dict[str, Any]],
    keywords_path: str | Path = "config/keywords.yaml",
    limit: int | None = None,
) -> list[dict[str, Any]]:
    processed = process_items(items, keywords_path, limit=limit)
    return processed["items"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Deduplicate, classify, and rank fetched items.")
    parser.add_argument("--input", default="data/raw.json")
    parser.add_argument("--output", default="data/processed.json")
    parser.add_argument("--keywords", default="config/keywords.yaml")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"))
    args = parser.parse_args()

    input_path = Path(args.input)
    rows = load_jsonl(input_path) if input_path.suffix == ".jsonl" else load_json(input_path)
    processed = process_items(rows, args.keywords, report_date=args.date, limit=args.limit if args.limit > 0 else None)
    save_json(args.output, processed)
    print(f"wrote {processed['counts']['processed']} processed items to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
