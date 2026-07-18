from __future__ import annotations

from pathlib import Path

import yaml

from rank import process_items


def make_item(title: str, summary: str) -> dict:
    return {
        "id": title.lower().replace(" ", "-"),
        "title": title,
        "summary": summary,
        "url": "https://arxiv.org/abs/2601.00001",
        "published_at": "2026-07-18T00:00:00+00:00",
        "authors": ["Test Author"],
        "tags": [],
        "metrics": {},
        "metadata": {},
        "source": {"id": "fixture_arxiv", "name": "Fixture arXiv", "type": "arxiv", "kind": "primary", "source_role": "paper_source"},
    }


def test_research_profile_classification_cases() -> None:
    data = yaml.safe_load(Path("tests/fixtures/research_profile_cases.yaml").read_text(encoding="utf-8"))
    for case in data["cases"]:
        processed = process_items([make_item(case["title"], case["summary"])], report_date="2026-07-18")
        item = processed["items"][0]
        primary = item["primary_category"]["id"]
        matched = {entry["id"] for entry in item.get("matched_sections", []) if entry.get("id")}
        if "expect_primary" in case:
            assert primary == case["expect_primary"], case["title"]
        if "expect_any" in case:
            assert matched.intersection(set(case["expect_any"])), case["title"]
        if "reject_primary" in case:
            assert primary != case["reject_primary"], case["title"]
