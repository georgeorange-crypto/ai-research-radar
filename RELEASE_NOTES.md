# AI Research Radar v0.1.0 — Daily Research Intelligence MVP

## What this release is

This is the first daily-usable MVP of AI Research Radar. It automatically
collects AI academic and technology signals, ranks them for research value, and
generates a daily Markdown and GitHub Pages report.

It is not trying to be feature-complete. The goal of v0.1.0 is a stable daily
research intelligence pipeline with safe defaults.

## Core features

- Multi-source collection
- Daily Markdown report
- GitHub Pages report
- Research-priority ranking
- LLM summary support
- Single-model default mode
- Cost guard basics
- Source health reporting
- Benchmark and GitHub project discovery
- Classic paper recall

## Default cost-safe mode

The default mode is single.
role_pipeline is experimental and should not be enabled for daily scheduled runs unless the user explicitly accepts higher API cost.

role_pipeline may call multiple models per item and can be expensive. It is
kept as an advanced experiment, not as the scheduled daily default.

## Setup

Configure GitHub Actions with repository Secrets and Variables. Do not put API
keys in release notes, README examples, or committed files.

Secrets:

- `OPENAI_API_KEY`
- or `KIMI_API_KEY` / `DEEPSEEK_API_KEY` / `GLM_API_KEY`

Variables:

- `OPENAI_BASE_URL`
- `OPENAI_MODEL`

Recommended:

```env
MODEL_MODE=single
OPENAI_SUMMARY_BUDGET=3
MAX_OUTPUT_TOKENS=250
MAX_EVIDENCE_CHARS=1600
```

## How to run locally

```bash
pip install -r requirements.txt
python run.py
```

## How to trigger GitHub Actions manually

Open GitHub -> Actions -> Daily AI Research Radar -> Run workflow.

## Known limitations

- Not yet a full web application
- Ranking still needs feedback loop
- No interactive dashboard yet
- role_pipeline can be expensive
- Some source parsers may fail silently or return 0 items
- Ranking still sometimes overweights Agent / video diffusion items
- Context memory papers such as STALE / Q-RAG may need stronger promotion rules
- GitHub awesome-list repositories may still be noisy
- Meta AI Blog parser may return 0 items

## Next milestones

- v0.2.0: ranking and cost guard improvements
- v0.3.0: feedback loop and recommender architecture
- v0.4.0: FastAPI + React local web app
- v1.0.0: stable research intelligence application
