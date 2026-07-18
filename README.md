# AI Research Radar

AI Research Radar is George's daily academic and technical intelligence pipeline.
It collects research signals, ranks them against a personal research profile,
generates Markdown/HTML reports, and publishes the latest report with GitHub
Pages.

Current version: v0.2.0 — George Research Profile v2

GitHub Pages:
[https://georgeorange-crypto.github.io/ai-research-radar/](https://georgeorange-crypto.github.io/ai-research-radar/)

## George Research Profile v2

The v0.2 mission is high-performance AI systems and infrastructure for agentic
and embodied intelligence. The five P0 tracks are:

- AI Systems / HPC / Distributed Training & Inference
- GPU-Centric I/O / Networking / Storage
- Compression / Reliability for AI Infrastructure
- Agent Runtime / RL Infrastructure / Scheduling
- Embodied Intelligence / VLA / World Models

The profile lives in `config/research_profile.yaml`. Edit that file first when
changing George's long-term research direction, active projects, track terms,
context gates, co-occurrence rules, or MUST_READ buckets.

Legacy directions such as context compression, generic agents, open-world
learning, model distillation, CV, NLP, RL, model architecture, and benchmarks are
kept as supporting tracks. v0.2 is intentionally additive.

## Quick Start

```bash
pip install -r requirements.txt
python run.py
```

Compatible commands:

```bash
python run.py
python run.py --date YYYY-MM-DD
```

Generated artifacts include:

- `report.md`
- `index.html`
- `reports/daily/latest.md`
- `reports/daily/YYYY/MM/YYYY-MM-DD.md`
- `data/raw/YYYY-MM-DD.jsonl`
- `data/processed/YYYY-MM-DD.json`

## Source Architecture

v0.2 separates entity registration from active collection.

- Entity registries: `config/associations.yaml`, `config/venues.yaml`,
  `config/organizations.yaml`, `config/people.yaml`
- Active collectors: stable RSS/API/Atom/JSON/HTML selectors in
  `config/sources.yaml`
- Discovery and metadata APIs: OpenAlex, Crossref, Semantic Scholar, and DBLP
  adapters exist but are disabled by default unless explicitly enabled
- Verification sources: primary papers, DOI pages, conference pages, official
  blogs, official profiles, and official organization pages

Adding a registry entry does not automatically make it a daily crawler.

## Feedback

GitHub Pages is static, so v0.2 records feedback locally:

```bash
python feedback.py rate ITEM_ID highly_relevant
python feedback.py rate ITEM_ID irrelevant
python feedback.py follow-author AUTHOR_ID
python feedback.py mute-source SOURCE_ID
```

Events are written to `data/feedback/events.jsonl` and affect ranking through a
small explainable feedback score. If the file is missing, the radar falls back to
the cold-start research profile.

## LLM Cost Control

Default mode is `single`. `role_pipeline` still exists but is intentionally
expensive because it may call multiple models per item.

Recommended daily settings:

```env
MODEL_MODE=single
OPENAI_SUMMARY_BUDGET=3
MAX_OUTPUT_TOKENS=250
MAX_EVIDENCE_CHARS=1600
```

Provider fallback is safe by default: invalid providers are disabled for the
current run, the next configured provider is tried, and the report falls back to
local summaries if all providers fail. Do not commit API keys.

## Testing

```bash
python -m pytest
python run.py --date 2026-07-18 --skip-weekly --skip-monthly --skip-index
```

Default tests use mock network responses. Manual integration tests may enable
external APIs, but CI should not depend on public network availability.

## More Docs

- `docs/RESEARCH_PROFILE.md`
- `docs/SOURCE_REGISTRY.md`
- `docs/RANKING_AND_FEEDBACK.md`
- `docs/ADDING_A_SOURCE.md`
- `PROFILE_MIGRATION.md`
