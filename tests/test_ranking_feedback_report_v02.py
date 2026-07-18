from __future__ import annotations

from pathlib import Path

from rank import process_items
from summarize import generate_report


def item(title: str, summary: str, source_id: str = "fixture") -> dict:
    return {
        "id": title.lower().replace(" ", "-"),
        "title": title,
        "summary": summary,
        "url": f"https://arxiv.org/abs/{abs(hash(title)) % 100000}.00001",
        "published_at": "2026-07-18T00:00:00+00:00",
        "authors": ["Test Author"],
        "tags": [],
        "metrics": {},
        "metadata": {},
        "source": {"id": source_id, "name": source_id, "type": "arxiv", "kind": "primary", "source_role": "paper_source"},
    }


def test_must_read_diversity_and_report_snapshot() -> None:
    rows = [
        item("Distributed Training Runtime for AI Datacenters", "AI systems for GPU cluster scheduling and distributed training."),
        item("GPUDirect Storage Checkpoint I/O", "GPU-aware storage with GPUDirect Storage and distributed checkpoint I/O."),
        item("Agent Runtime Scheduling for RL Rollouts", "Agent runtime, rollout engine, resource admission, and RL infrastructure."),
        item("Vision-Language-Action World Model for Robots", "VLA robot policy and world model for robot planning."),
        item("Generic Agentic Mathematical Reasoning Benchmark", "A benchmark for agentic mathematical reasoning."),
    ]
    processed = process_items(rows, report_date="2026-07-18")
    must = [row for row in processed["items"] if row.get("reading_tier") == "MUST_READ"]
    assert len(must) <= 3
    assert any(row["primary_category"]["id"] in {"ai_systems_hpc", "gpu_data_path_storage", "agent_rl_infrastructure", "embodied_world_models"} for row in must)
    out_dir = Path(".test-output")
    out_dir.mkdir(exist_ok=True)
    report_path = out_dir / "daily.md"
    rendered = generate_report(processed, report_path, report_date="2026-07-18", latest_path=None, archive_latest=False, generate_html=False)
    assert "AI 系统 / HPC / 分布式训练与推理" in rendered
    assert "GPU 中心 I/O / 网络 / 存储" in rendered
    assert "学者雷达" in rendered
    assert "公司研究雷达" in rendered
    assert "来源健康状态" in rendered
    assert "项目相关性" in rendered


def test_processed_json_has_v02_defaults() -> None:
    processed = process_items([item("Erasure Coding for Distributed Checkpoint Storage", "Erasure coding, checksum, distributed storage, and checkpoint recovery.")], report_date="2026-07-18")
    row = processed["items"][0]
    assert isinstance(row.get("track_relevance"), dict)
    assert isinstance(row.get("project_relevance"), dict)
    assert "feedback_score" in row["scores"]
    assert "topic_drift_risk" in row["scores"]
    assert "source_provenance" in row
