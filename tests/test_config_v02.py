from __future__ import annotations

from pathlib import Path

import yaml

from rank import load_radar_config, section_configs
from fetch import FETCHERS


LEGACY_SOURCE_IDS = {
    "hf_daily_papers",
    "arxiv_ai_ml",
    "openreview_core",
    "papers_with_code_trending",
    "github_ai_projects",
}

LEGACY_SECTION_IDS = {
    "context_compression_memory",
    "agents",
    "open_world_learning",
    "model_distillation",
    "cv",
    "nlp",
    "rl",
    "model_architecture",
    "learning_methods",
    "benchmark_evaluation",
    "github_projects",
    "classics",
    "institutional_updates",
}

LEGACY_KEYWORDS = {
    "context compression",
    "long context",
    "agent memory",
    "llm agent",
    "open-world learning",
    "knowledge distillation",
    "model compression",
    "benchmark",
    "github",
}


def load_yaml(path: str) -> dict:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}


def flatten_terms(section: dict) -> set[str]:
    terms = set()
    for key in ["terms", "strong_terms", "supporting_terms"]:
        terms.update(str(term).lower() for term in section.get(key, []) or [])
    return terms


def test_yaml_files_parse_and_ids_are_unique() -> None:
    for path in Path("config").glob("*.yaml"):
        load_yaml(str(path))
    config = load_radar_config("config/keywords.yaml")
    for key in ["sources", "tracks", "venues", "organizations", "people", "associations"]:
        ids = [row["id"] for row in config.get(key, []) if isinstance(row, dict) and row.get("id")]
        assert len(ids) == len(set(ids)), key


def test_legacy_superset_and_new_p0_tracks() -> None:
    config = load_radar_config("config/keywords.yaml")
    source_ids = {row["id"] for row in config.get("sources", []) if row.get("id")}
    section_ids = {row["id"] for row in section_configs(config)}
    terms = set()
    for section in section_configs(config):
        terms |= flatten_terms(section)
    assert LEGACY_SOURCE_IDS <= source_ids
    assert LEGACY_SECTION_IDS <= section_ids
    assert LEGACY_KEYWORDS <= terms
    assert {
        "ai_systems_hpc",
        "gpu_data_path_storage",
        "compression_reliability",
        "agent_rl_infrastructure",
        "embodied_world_models",
    } <= section_ids


def test_active_collectors_have_fetchers() -> None:
    config = load_radar_config("config/keywords.yaml")
    for source in config.get("sources", []):
        if source.get("enabled", True):
            assert source.get("type") in FETCHERS, source.get("id")
