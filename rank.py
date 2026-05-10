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

PAPER_TIERS = {"MUST_READ", "SKIM", "WATCH", "ARCHIVE", "IGNORE"}
GITHUB_ACTIONS = {"study_code", "use_as_baseline", "read_readme", "save"}
CONTEXT_SECTION_IDS = {"context_compression_memory", "context_compression", "context_memory"}
MAINLINE_SECTION_IDS = {"context_compression_memory", "context_compression", "agents", "open_world_learning", "model_distillation"}
GROUNDING_LEVELS = {"title_only", "abstract_only", "full_text", "repo_readme"}
GENERIC_MATCH_TERMS = {
    "benchmark",
    "dataset",
    "evaluation",
    "framework",
    "inference",
    "environment",
    "systems",
    "github",
    "code release",
    "open source",
    "open-source",
    "nlp",
    "robotics",
}

TITLE_CATEGORY_OVERRIDES = [
    (
        "stale: can llm agents know when their memories are no longer valid",
        "context_compression_memory",
        ["Agent Memory", "Belief Update", "Benchmark", "Long Context"],
    ),
    (
        "adaptive parallel reasoning",
        "agents",
        ["Reasoning", "Inference-time Scaling", "Long Context", "Planning"],
    ),
    (
        "hitting time isomorphism",
        "rl",
        ["Learning Methods", "Long-horizon Planning", "Foundation Policies"],
    ),
    (
        "continuous-time distribution matching",
        "model_distillation",
        ["Diffusion Distillation", "Efficient Generation", "CV"],
    ),
    (
        "nvidia/model-optimizer",
        "github_projects",
        ["Model Compression", "Quantization", "Tool Library"],
    ),
    (
        "dinorankclip",
        "model_distillation",
        ["CV / VLM", "DINOv3 Distillation", "Ranking Consistency"],
    ),
    (
        "efficient serving for dynamic agent workflows",
        "context_compression_memory",
        ["Agent Infrastructure", "KV Cache", "Serving"],
    ),
    (
        "video action differencing",
        "benchmark_evaluation",
        ["Video Understanding", "Action Evaluation"],
    ),
    (
        "spatialepibench",
        "benchmark_evaluation",
        ["Spatial Epidemiology", "Scientific Evaluation"],
    ),
    (
        "medarabench",
        "benchmark_evaluation",
        ["Medical QA", "Arabic NLP", "Dataset"],
    ),
    (
        "workflow fidelity",
        "benchmark_evaluation",
        ["Agent Evaluation", "Payment Workflow", "Trajectory Fidelity"],
    ),
]

FORCE_WATCH_TITLE_PATTERNS = [
    "recursive agent optimization",
    "q-rag",
    "mia-signature",
    "long context pre-training with lighthouse attention",
]

FORCE_MIN_WATCH_TITLE_PATTERNS = [
    "efficient serving for dynamic agent workflows",
    "dinorankclip",
]

TOP_OFFICIAL_RELEASE_HINTS = {
    "openai",
    "anthropic",
    "deepmind",
    "google",
    "meta",
    "microsoft",
    "nvidia",
    "apple",
}

MUST_BUCKET_ORDER = ["context_memory", "agentic_planning", "open_or_distill"]


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


def title_text(item: dict[str, Any]) -> str:
    return normalize_title(item.get("title", ""))


def contains_any(text: str, patterns: list[str] | set[str]) -> bool:
    normalized = normalize_title(text)
    return any(normalize_title(pattern) in normalized for pattern in patterns)


def section_lookup(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {section["id"]: section for section in section_configs(config)}


def category_entry(section_id: str, config: dict[str, Any], *, score: float = 0.0, terms: list[str] | None = None) -> dict[str, Any]:
    section = section_lookup(config).get(section_id, {"title": section_id, "group": "other"})
    return {
        "id": section_id,
        "title": section.get("title", section_id),
        "group": section.get("group", "other"),
        "score": round(score, 3),
        "matched_terms": terms or [],
    }


def custom_tag_entry(title: str) -> dict[str, Any]:
    tag_id = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
    return {"id": tag_id, "title": title, "group": "tag", "score": 1.0, "matched_terms": [title]}


def is_repository_item(item: dict[str, Any]) -> bool:
    url = item.get("url", "")
    source_type = item.get("source", {}).get("type")
    return source_type == "github_search" or "github.com" in urlparse(url).netloc.lower()


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


def ensure_grounding_metadata(item: dict[str, Any]) -> None:
    if not is_repository_item(item):
        return
    metadata = dict(metadata_dict(item))
    if item.get("summary") and not metadata.get("github_description"):
        metadata["github_description"] = item.get("summary", "")
    item["metadata"] = metadata


def infer_grounding_level(item: dict[str, Any]) -> str:
    if is_repository_item(item):
        return "repo_readme" if repo_readme_summary(item) else "title_only"
    summary = str(item.get("abstract") or item.get("summary") or "").strip()
    if not summary:
        return "title_only"
    source_type = str(item.get("source", {}).get("type", "")).lower()
    if source_type in {"arxiv", "openreview", "hf_daily_papers", "hf_papers_page"}:
        return "abstract_only"
    return "full_text"


def is_benchmark_like(item: dict[str, Any]) -> bool:
    text = item_text(item)
    return any(
        term_matches(term, text)
        for term in [
            "benchmark",
            "dataset",
            "evaluation",
            "leaderboard",
            "workflow fidelity",
            "question answering dataset",
            "test set",
        ]
    )


GENERIC_INSTITUTIONAL_LINK_TITLES = {
    "research",
    "education",
    "products",
    "featured",
    "learn more",
    "download press kit",
    "stanford home",
    "maps directions",
    "search stanford",
    "emergency info",
    "terms of use",
    "copyright",
    "trademarks",
    "non discrimination",
    "accessibility",
    "get involved with hai",
    "support hai",
    "subscribe to email",
    "school of computer science",
    "economic futures",
}


def is_generic_institutional_link(item: dict[str, Any]) -> bool:
    title = title_text(item)
    if title in GENERIC_INSTITUTIONAL_LINK_TITLES:
        return True
    return title.startswith(("about ", "about:", "education ", "education:", "student ", "student:"))


def is_institutional_update(item: dict[str, Any]) -> bool:
    source = item.get("source", {})
    source_type = source.get("type")
    if source_type in {"arxiv", "openreview", "github_search", "hf_daily_papers", "hf_papers_page"}:
        return False
    source_id = str(source.get("id", "")).lower()
    source_name = str(source.get("name", "")).lower()
    source_url = str(source.get("url", "")).lower()
    item_url = str(item.get("url", "")).lower()
    official_sources = [
        "openai",
        "anthropic",
        "deepmind",
        "google_research",
        "meta_ai",
        "microsoft",
        "nvidia",
        "apple",
        "stanford",
        "mit",
        "bair",
        "princeton",
        "cmu",
        "neurips",
        "icml",
        "iclr",
        "acl",
        "emnlp",
        "cvpr",
        "iccv",
        "eccv",
        "corl",
    ]
    official = any(token in source_id or token in source_name or token in source_url or token in item_url for token in official_sources)
    if not official or is_generic_institutional_link(item):
        return False

    title = title_text(item)
    url_text = f"{source_url} {item_url}"
    official_blog_markers = [
        "/blog/",
        "/blogs/",
        "/index/",
        "/news/",
        "/research/blog",
        "research.google/blog",
        "microsoft.com/en-us/research/blog",
        "blogs.nvidia.com/blog",
        "deepmind.google/blog",
        "machinelearning.apple.com/research",
    ]
    update_terms = [
        "announcement",
        "announcements",
        "announcing",
        "introducing",
        "release",
        "launched",
        "launch",
        "technical report",
        "research update",
        "lab",
        "institute",
        "partnership",
        "conference",
        "award",
        "fellowship",
        "supercomputer",
        "red teaming",
        "red-teaming",
    ]
    if source_type == "rss" and any(marker in url_text for marker in official_blog_markers):
        return True
    return any(marker in url_text for marker in official_blog_markers) or any(term in title for term in update_terms)


def title_matches(item: dict[str, Any], pattern: str) -> bool:
    return normalize_title(pattern) in title_text(item)


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


def best_alternative_section(
    scores: dict[str, float],
    by_id: dict[str, dict[str, Any]],
    *,
    exclude: set[str] | None = None,
) -> str | None:
    exclude = exclude or set()
    for section_id, score in sorted(scores.items(), key=lambda pair: pair[1], reverse=True):
        if score <= 0 or section_id in exclude or section_id not in by_id:
            continue
        return section_id
    return None


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

    extra_tag_titles: list[str] = []
    override_exact_tags = False
    for pattern, override_id, tags in TITLE_CATEGORY_OVERRIDES:
        if title_matches(item, pattern):
            primary_id = override_id
            extra_tag_titles.extend(tags)
            override_exact_tags = True
            break

    if is_repository_item(item):
        primary_id = "github_projects"
        extra_tag_titles.append("Tool Library")
    elif primary_id != "benchmark_evaluation" and is_benchmark_like(item):
        title = title_text(item)
        if any(token in title for token in ["benchmark", "bench", "dataset", "evaluation", "eval"]):
            primary_id = "benchmark_evaluation"
    elif primary_id == "github_projects":
        alternative_id = best_alternative_section(
            scores,
            by_id,
            exclude={"github_projects", "institutional_updates", "classics"},
        )
        primary_id = alternative_id or (fallback_id if fallback_id in by_id else "highlights")
        extra_tag_titles.append("Open Source Signal")
    if primary_id == "institutional_updates" and not is_institutional_update(item):
        alternative_id = best_alternative_section(
            scores,
            by_id,
            exclude={"institutional_updates", "github_projects", "classics"},
        )
        primary_id = alternative_id or (fallback_id if fallback_id in by_id else "highlights")
        extra_tag_titles.append("Official Source Mention")

    primary = by_id.get(primary_id, {"title": primary_id, "group": "other"})
    if not any(entry.get("id") == primary_id for entry in matched_section_entries):
        matched_section_entries.insert(
            0,
            category_entry(
                primary_id,
                config,
                score=normalized_scores.get(primary_id, 1.0 if extra_tag_titles else 0.0),
                terms=hits_by_section.get(primary_id, []),
            ),
        )

    secondary_entries = [] if override_exact_tags else [
        entry
        for entry in matched_section_entries
        if entry.get("id") != primary_id and entry.get("id") != "institutional_updates"
    ]
    seen_secondary = {entry.get("title") for entry in secondary_entries}
    for tag_title in extra_tag_titles:
        if tag_title not in seen_secondary:
            secondary_entries.append(custom_tag_entry(tag_title))
            seen_secondary.add(tag_title)
    matched_sections = [primary.get("title", primary_id)] + [section["title"] for section in secondary_entries]
    return (
        primary_id,
        primary.get("title", primary_id),
        primary.get("group", "other"),
        normalized_scores,
        matched_terms,
        matched_sections,
        secondary_entries,
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
    return is_repository_item(item)


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
    ensure_grounding_metadata(item)
    item["grounding_level"] = infer_grounding_level(item)
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

    primary_category = {
        "id": section_id,
        "title": section_title,
        "group": section_group,
    }
    item["primary_category"] = primary_category
    item["primary_section"] = primary_category
    item["section_scores"] = section_scores
    item["secondary_tags"] = matched_section_entries
    item["matched_sections"] = [primary_category, *matched_section_entries]
    item["matched_keywords"] = matched_terms
    item["matched_focus_areas"] = matched_sections
    item["is_open_source_project"] = is_open_source_project(item)
    item["is_repository_item"] = is_repository_item(item)
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
    if tier in GITHUB_ACTIONS:
        return "GitHub 项目使用项目动作分层，不进入论文深读队列。"
    if tier == "MUST_READ":
        return "与四条主线直接相关，且通过编辑规则进入当日最多 3 篇深读名额。"
    if tier == "SKIM":
        return "质量和相关性足够高，适合快速略读后决定是否升级。"
    if tier == "WATCH":
        return "方向相关、值得追踪，但今天不安排深读。"
    if tier == "ARCHIVE":
        return "保留到资料库，当前优先级低于 WATCH。"
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


def primary_category_id(item: dict[str, Any]) -> str:
    return item.get("primary_category", item.get("primary_section", {})).get("id", "")


def primary_category_group(item: dict[str, Any]) -> str:
    return item.get("primary_category", item.get("primary_section", {})).get("group", "")


def primary_matched_terms(item: dict[str, Any]) -> list[str]:
    primary_id = primary_category_id(item)
    for section in item.get("matched_sections", []) or []:
        if section.get("id") == primary_id:
            return [str(term).lower() for term in section.get("matched_terms", [])]
    return [str(term).lower() for term in item.get("matched_keywords", [])]


def is_keyword_only_match(item: dict[str, Any]) -> bool:
    terms = primary_matched_terms(item)
    if not terms:
        return True
    non_generic = [term for term in terms if term.lower() not in GENERIC_MATCH_TERMS]
    return len(non_generic) == 0 or (len(non_generic) == 1 and len(terms) <= 2)


def is_pure_tool_library(item: dict[str, Any]) -> bool:
    if is_repository_item(item):
        return True
    text = item_text(item)
    title = title_text(item)
    return (
        primary_category_id(item) == "github_projects"
        or ("toolkit" in text and "paper" not in title)
        or ("library" in text and "benchmark" not in title and "method" not in title)
    )


def is_deep_read_source(item: dict[str, Any]) -> bool:
    source = item.get("source", {})
    source_type = str(source.get("type", "")).lower()
    if source_type in {"arxiv", "openreview", "hf_daily_papers", "hf_papers_page"}:
        return True
    if source_type == "rss" and source.get("kind") == "primary":
        return True
    return False


def is_top_official_release(item: dict[str, Any]) -> bool:
    source = item.get("source", {})
    text = " ".join(
        [
            str(source.get("id", "")),
            str(source.get("name", "")),
            str(source.get("url", "")),
            str(item.get("url", "")),
        ]
    ).lower()
    return source.get("kind") == "primary" and any(hint in text for hint in TOP_OFFICIAL_RELEASE_HINTS)


def force_watch(item: dict[str, Any]) -> bool:
    return any(title_matches(item, pattern) for pattern in FORCE_WATCH_TITLE_PATTERNS)


def force_min_watch(item: dict[str, Any]) -> bool:
    return force_watch(item) or any(title_matches(item, pattern) for pattern in FORCE_MIN_WATCH_TITLE_PATTERNS)


def editorial_priority_score(item: dict[str, Any]) -> float:
    scores = item.get("scores", {})
    primary_id = primary_category_id(item)
    text = item_text(item)
    priority = (
        scores.get("personal_score", 0.0) * 0.45
        + scores.get("global_score", 0.0) * 0.20
        + scores.get("novelty", 0.0) * 0.15
        + scores.get("credibility", 0.0) * 0.10
        + scores.get("evidence_strength", 0.0) * 0.10
    )

    if primary_id in CONTEXT_SECTION_IDS and any(term in text for term in ["agent memory", "memory validity", "belief update", "kv cache", "long context"]):
        priority += 0.16
    if primary_id == "agents" and any(term in text for term in ["agent evaluation", "agentic rl", "long-horizon", "long horizon", "workflow fidelity", "trajectory", "safety"]):
        priority += 0.12
    if primary_id == "model_distillation" and any(term in text for term in ["diffusion distillation", "step distillation", "dinorankclip", "dino"]):
        priority += 0.06
    if item.get("source", {}).get("kind") == "primary":
        priority += 0.04
    if primary_category_group(item) in {"primary_research", "core_focus"}:
        priority += 0.04
    if primary_id in {"benchmark_evaluation"} and not any(term in text for term in ["agent evaluation", "safety", "workflow fidelity", "long-horizon"]):
        priority -= 0.08
    if is_pure_tool_library(item):
        priority -= 0.35
    if is_keyword_only_match(item):
        priority -= 0.10
    if force_watch(item):
        priority -= 0.15
    return clamp_score(priority)


def editorial_rank_key(item: dict[str, Any]) -> tuple[float, float, float, float]:
    scores = item.get("scores", {})
    return (
        editorial_priority_score(item),
        scores.get("novelty", 0.0),
        scores.get("credibility", 0.0),
        scores.get("personal_score", 0.0),
    )


def must_bucket(item: dict[str, Any]) -> str | None:
    primary_id = primary_category_id(item)
    text = item_text(item)
    memory_terms = [
        "context compression",
        "agent memory",
        "memory validity",
        "belief update",
        "kv cache",
        "kv-cache",
        "cache reuse",
    ]
    planning_terms = [
        "agentic rl",
        "long-horizon",
        "long horizon",
        "planning",
        "trajectory",
        "workflow",
        "environment",
        "reinforcement learning",
    ]
    agent_memory_terms = [
        "context compression",
        "agent memory",
        "memory validity",
        "belief update",
    ]
    if primary_id in CONTEXT_SECTION_IDS:
        return "context_memory"
    if primary_id == "agents":
        if any(term in text for term in agent_memory_terms):
            return "context_memory"
        if any(term in text for term in planning_terms):
            return "agentic_planning"
        return "agentic_planning"
    if primary_id == "rl" and any(term in text for term in planning_terms):
        return "agentic_planning"
    if primary_id in {"open_world_learning", "model_distillation"}:
        return "open_or_distill"
    if any(
        term in text
        for term in memory_terms
        + [
            "long context",
        ]
    ):
        return "context_memory"
    return None


def must_read_eligible(item: dict[str, Any]) -> bool:
    scores = item.get("scores", {})
    primary_id = primary_category_id(item)
    priority = editorial_priority_score(item)
    personal = scores.get("personal_score", 0.0)
    relevance = scores.get("research_relevance", 0.0)
    if ignore_reason(item):
        return False
    if primary_category_group(item) not in {"primary_research", "core_focus"}:
        return False
    if primary_id == "benchmark_evaluation":
        return False
    if not is_deep_read_source(item) or is_pure_tool_library(item) or force_watch(item):
        return False
    if primary_id in MAINLINE_SECTION_IDS and relevance < 0.80:
        return False
    if personal < 0.80 and not (is_top_official_release(item) and priority >= 0.94):
        return False
    return priority >= 0.80


def skim_eligible(item: dict[str, Any]) -> bool:
    scores = item.get("scores", {})
    priority = editorial_priority_score(item)
    return (
        not ignore_reason(item)
        and not force_watch(item)
        and (
            priority >= 0.72
            or scores.get("personal_score", 0) >= 0.72
            or scores.get("global_score", 0) >= 0.85
        )
    )


def github_project_action(item: dict[str, Any]) -> str:
    metrics = item.get("metrics", {})
    stars = metrics.get("stars", 0) or 0
    text = item_text(item)
    primary_id = primary_category_id(item)
    if any(term in text for term in ["model-optimizer", "model optimizer", "quantization", "pruning", "compression", "optimizer"]):
        return "study_code" if stars >= 500 or "library" in text or "toolkit" in text else "save"
    if stars >= 5000 and any(term in text for term in ["demo", "examples", "benchmark", "inference", "training"]):
        return "study_code"
    if primary_id in {"model_distillation", *CONTEXT_SECTION_IDS} or any(term in text for term in ["baseline", "evaluation suite", "benchmark suite"]):
        return "use_as_baseline"
    if stars >= 1000 or any(term in text for term in ["framework", "library", "toolkit"]):
        return "study_code"
    if stars >= 100:
        return "read_readme"
    if scores := item.get("scores", {}):
        if scores.get("actionability", 0) >= 0.55:
            return "save"
    return "save"


def assign_reading_tiers(items: list[dict[str, Any]]) -> None:
    for item in items:
        item["editorial_priority"] = round(editorial_priority_score(item), 3)

    for item in items:
        if is_repository_item(item):
            action = github_project_action(item)
            item["github_action"] = action
            item["reading_tier"] = action
            item["reading_tier_reason"] = "GitHub repository is routed to the open-source project section, not the deep-read queue."
            item["worth_deep_read"] = False

    paper_items = sorted(
        [item for item in items if not is_repository_item(item)],
        key=editorial_rank_key,
        reverse=True,
    )
    for item in paper_items:
        item["reading_tier"] = None
        item["worth_deep_read"] = False

    must_selected: list[dict[str, Any]] = []
    used_ids: set[str] = set()
    for bucket in MUST_BUCKET_ORDER:
        candidates = [
            item
            for item in paper_items
            if id(item) not in used_ids and must_read_eligible(item) and must_bucket(item) == bucket
        ]
        if not candidates:
            continue
        chosen = candidates[0]
        must_selected.append(chosen)
        used_ids.add(id(chosen))
        if len(must_selected) >= MUST_READ_LIMIT:
            break

    if len(must_selected) < MUST_READ_LIMIT:
        for item in paper_items:
            if id(item) in used_ids or not must_read_eligible(item):
                continue
            must_selected.append(item)
            used_ids.add(id(item))
            if len(must_selected) >= MUST_READ_LIMIT:
                break

    for item in must_selected:
        item["reading_tier"] = "MUST_READ"
        item["reading_tier_reason"] = tier_reason(item, "MUST_READ")
        item["worth_deep_read"] = True

    skim_count = 0
    for item in paper_items:
        if item.get("reading_tier") == "MUST_READ":
            continue
        scores = item.get("scores", {})
        reason = ignore_reason(item)
        if reason:
            tier = "IGNORE"
            item["reading_tier_reason"] = reason
            item["reading_tier"] = tier
            item["worth_deep_read"] = False
            continue

        priority = editorial_priority_score(item)
        if skim_eligible(item) and skim_count < SKIM_LIMIT:
            tier = "SKIM"
            skim_count += 1
        elif (
            force_min_watch(item)
            or priority >= 0.62
            or scores.get("research_relevance", 0) >= 0.72
            or (
                primary_category_group(item) in {"primary_research", "core_focus"}
                and scores.get("personal_score", 0) >= 0.68
            )
        ):
            tier = "WATCH"
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
            and primary_category_id(item) == section["id"]
            and not is_repository_item(item)
            and (section["id"] != "institutional_updates" or is_institutional_update(item))
        ]
        section_items.sort(key=score_rank_key, reverse=True)
        sections.append({**section, "items": section_items})
    return sections


def select_github_projects(items: list[dict[str, Any]], limit: int = 5) -> list[dict[str, Any]]:
    action_rank = {
        "use_as_baseline": 5,
        "study_code": 4,
        "read_readme": 3,
        "save": 2,
    }
    projects = [item for item in items if item.get("reading_tier") != "IGNORE" and is_repository_item(item)]
    projects.sort(
        key=lambda item: (
            action_rank.get(item.get("github_action") or item.get("reading_tier"), 0),
            item.get("scores", {}).get("actionability", 0),
            item.get("scores", {}).get("community_signal", 0),
            item.get("metrics", {}).get("stars", 0) or 0,
            item.get("scores", {}).get("personal_score", 0),
        ),
        reverse=True,
    )
    return projects[:limit]


CLASSIC_TOPIC_ALIASES = {
    "context_memory": "context_compression_memory",
    "context_compression": "context_compression_memory",
    "context_compression_memory": "context_compression_memory",
    "long_context": "context_compression_memory",
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
    0: ("Context Compression / Long Context / Memory", {"context_compression_memory", "context_compression", "long_context"}),
    1: ("Agents", {"agents", "planning", "tool_use"}),
    2: ("Open-World Learning", {"open_world_learning", "open_set_recognition", "continual_learning"}),
    3: ("Distillation", {"model_distillation", "model_compression", "efficient_training"}),
    4: ("RL", {"rl"}),
    5: ("CV / NLP / Architecture", {"cv", "nlp", "model_architecture"}),
    6: ("AI Systems / Interpretability / AI for Science", {"ai_systems", "interpretability", "ai_for_science", "biology"}),
}

CLASSIC_GENERIC_TERMS = {
    "nlp",
    "language model",
    "transformer",
    "attention",
    "model architecture",
    "model_architecture",
    "cv",
    "computer vision",
}


def normalized_topic_tags(paper: dict[str, Any]) -> set[str]:
    tags = {str(tag).strip().lower() for tag in paper.get("topic_tags", []) if str(tag).strip()}
    return {CLASSIC_TOPIC_ALIASES.get(tag, tag) for tag in tags} | tags


def related_modern_keywords(paper: dict[str, Any]) -> set[str]:
    return {str(keyword).strip().lower() for keyword in paper.get("related_modern_keywords", []) if str(keyword).strip()}


def item_keywords(item: dict[str, Any]) -> set[str]:
    return {str(keyword).strip().lower() for keyword in item.get("matched_keywords", []) if str(keyword).strip()}


def item_primary_topic(item: dict[str, Any]) -> str:
    primary_id = primary_category_id(item).lower()
    return CLASSIC_TOPIC_ALIASES.get(primary_id, primary_id)


def classic_connection_terms(paper: dict[str, Any], item: dict[str, Any]) -> list[str]:
    text = item_text(item)
    keyword_hits = [
        keyword
        for keyword in related_modern_keywords(paper)
        if keyword and keyword not in CLASSIC_GENERIC_TERMS and (term_matches(keyword, text) or keyword in item_keywords(item))
    ]
    section_hits = normalized_topic_tags(paper).intersection({item_primary_topic(item)})
    return sorted(set(keyword_hits + list(section_hits)))[:8]


def classic_relation_score(paper: dict[str, Any], item: dict[str, Any]) -> tuple[float, list[str]]:
    terms = classic_connection_terms(paper, item)
    if not terms:
        return 0.0, []
    section_bonus = 2.5 * len(normalized_topic_tags(paper).intersection({item_primary_topic(item)}))
    keyword_bonus = 0.75 * len(set(terms).intersection(related_modern_keywords(paper)))
    item_bonus = item.get("scores", {}).get("personal_score", 0.0)
    specific_bonus = classic_specific_bonus(paper, item, terms)
    return section_bonus + keyword_bonus + item_bonus + specific_bonus, terms


def classic_specific_bonus(paper: dict[str, Any], item: dict[str, Any], terms: list[str]) -> float:
    item_text_value = item_text(item)
    paper_text = " ".join(
        [
            normalize_title(str(paper.get("title", ""))),
            normalize_title(str(paper.get("bibtex", ""))),
            " ".join(related_modern_keywords(paper)),
        ]
    )
    if "dinorankclip" in item_text_value:
        if "rankclip" in paper_text:
            return 4.0
        if "clip" in paper_text and "rankclip" not in paper_text:
            return 3.4
        if "dino" in paper_text:
            return 3.2
        if "knowledge distillation" in paper_text or "distilling" in paper_text:
            return 3.0
        if "lora" in paper_text or "low rank" in paper_text:
            return -2.0
    if any(term in {"knowledge distillation", "distillation", "teacher student"} for term in terms):
        if "lora" in paper_text or "low rank" in paper_text:
            return -0.8
    return 0.0


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


def concept_connection_for_classic(
    paper: dict[str, Any],
    related_items: list[tuple[dict[str, Any], list[str]]],
    rotation_label: str | None = None,
) -> dict[str, str]:
    topics = normalized_topic_tags(paper)
    titles = [item.get("title", "") for item, _ in related_items[:3]]
    today = "；".join(title for title in titles if title) or (rotation_label or "今天的相关条目")

    if "context_compression_memory" in topics:
        return {
            "inherits": f"{today} 延续了经典工作里的核心问题：有限上下文、外部记忆与状态复用如何支撑更长程的推理。",
            "challenges": "它挑战的是静态检索、固定窗口或只读记忆的假设，转向会随新证据更新的工作记忆和缓存管理。",
            "extends": "新场景从语言建模推进到 agent memory、动态 workflow 和长上下文服务系统。",
        }
    if "agents" in topics:
        return {
            "inherits": f"{today} 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。",
            "challenges": "它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。",
            "extends": "新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。",
        }
    if "open_world_learning" in topics:
        return {
            "inherits": f"{today} 继承了开放世界学习对未知类、分布漂移和持续更新的关注。",
            "challenges": "它挑战封闭标签集和一次性训练/测试划分的假设，更强调在线发现、语义漂移和真实部署反馈。",
            "extends": "新场景从传统视觉分类推进到多模态、开放词表和可复用 benchmark。",
        }
    if "model_distillation" in topics:
        return {
            "inherits": f"{today} 继承了经典压缩/蒸馏工作的问题：如何在更低计算成本下保留教师模型能力。",
            "challenges": "它挑战只做 logits matching 或静态小模型压缩的假设，转向轨迹、扩散过程、排序一致性和部署约束。",
            "extends": "新场景扩展到 few-step diffusion、VLM 预训练、量化剪枝和推理服务优化。",
        }
    if "rl" in topics:
        return {
            "inherits": f"{today} 延续了经典 RL 对序贯决策、策略优化和长期回报分配的研究问题。",
            "challenges": "它挑战在线交互充分、环境模型简单或奖励即时可见的假设，转向离线数据、foundation policies 和长程轨迹结构。",
            "extends": "新场景推进到多阶段规划、agentic RL 和复杂任务轨迹表示。",
        }
    return {
        "inherits": f"{today} 与这篇经典论文共享一个概念问题，而不仅是关键词重合。",
        "challenges": "需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。",
        "extends": "暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。",
    }


def build_classic_result(
    paper: dict[str, Any],
    config: dict[str, Any],
    related_items: list[tuple[dict[str, Any], list[str]]],
    connection: str,
    concept_connection: dict[str, str] | None = None,
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
        "concept_connection": concept_connection or concept_connection_for_classic(paper, related_items),
        "why_now": paper.get("why_classic", "用于把今天的新结果放回经典脉络中理解。"),
    }


def related_primary_topics(related_items: list[tuple[dict[str, Any], list[str]]]) -> set[str]:
    return {item_primary_topic(item) for item, _ in related_items if item_primary_topic(item)}


def select_classic_papers(
    items: list[dict[str, Any]],
    config: dict[str, Any],
    limit: int = 1,
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
        concept = concept_connection_for_classic(paper, related_items)
        connection = " ".join([concept["inherits"], concept["challenges"], concept["extends"]])
        selected.append((relation_score, int(paper.get("year", 0)), paper, related_items, connection))

    if not selected:
        rotation_label, rotation_tags = rotation_topic(report_date)
        rotation_topics = {CLASSIC_TOPIC_ALIASES.get(tag, tag) for tag in rotation_tags} | rotation_tags
        for paper in papers:
            topic_overlap = normalized_topic_tags(paper).intersection(rotation_topics)
            if not topic_overlap:
                continue
            concept = concept_connection_for_classic(paper, [], rotation_label)
            connection = (
                f"今天没有足够明确的 MUST_READ 经典连接，因此按星期主题轮换到 {rotation_label}。 "
                + " ".join([concept["inherits"], concept["challenges"], concept["extends"]])
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
    diverse: list[tuple[float, int, dict[str, Any], list[tuple[dict[str, Any], list[str]]], str]] = []
    used_topics: set[str] = set()
    for row in selected:
        topics = related_primary_topics(row[3])
        if topics and topics.issubset(used_topics):
            continue
        diverse.append(row)
        used_topics.update(topics)
        if len(diverse) >= limit:
            break
    if len(diverse) < limit:
        for row in selected:
            if row in diverse:
                continue
            diverse.append(row)
            if len(diverse) >= limit:
                break
    return [
        build_classic_result(paper, config, related_items, connection)
        for _, _, paper, related_items, connection in diverse[:limit]
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
    must_primary_mainlines = {
        primary_category_id(item)
        for item in scored
        if item.get("reading_tier") == "MUST_READ" and primary_category_id(item) in MAINLINE_SECTION_IDS
    }
    classic_limit = 2 if len(must_primary_mainlines) >= 2 else 1
    classic_revisit = select_classic_papers(scored, config, limit=classic_limit, report_date=report_date)

    return {
        "date": report_date or datetime.now().strftime("%Y-%m-%d"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "schema_version": 7,
        "counts": {
            "raw": len(items),
            "deduped": len(deduped),
            "processed": len(scored),
            "must_read": tier_counts.get("MUST_READ", 0),
            "skim": tier_counts.get("SKIM", 0),
            "watch": tier_counts.get("WATCH", 0),
            "archive": tier_counts.get("ARCHIVE", 0),
            "ignore": tier_counts.get("IGNORE", 0),
            "github_projects": len(github_projects),
            "clone_and_run": tier_counts.get("clone_and_run", 0),
            "study_code": tier_counts.get("study_code", 0),
            "use_as_baseline": tier_counts.get("use_as_baseline", 0),
            "read_readme": tier_counts.get("read_readme", 0),
            "save": tier_counts.get("save", 0),
            "github_archive": tier_counts.get("archive", 0),
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
