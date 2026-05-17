# AI Research Radar

AI Research Radar is a daily AI academic and technology intelligence pipeline.
It collects research signals, ranks them for a research-focused reader, generates
a Markdown daily report, and renders the latest report as a GitHub Pages page.

Current version: v0.1.0

GitHub Pages:
[https://georgeorange-crypto.github.io/ai-research-radar/](https://georgeorange-crypto.github.io/ai-research-radar/)

## Default Mode

Default mode: single

Do not use role_pipeline for daily automation unless you understand the API cost.
role_pipeline may call multiple models per item and can be expensive. It is not
the default mode.

## Core Capabilities

- Multi-source AI research collection
- Daily Markdown report generation
- GitHub Pages HTML report generation
- Research-priority ranking for LLM agents, context compression, open-world learning, and model distillation
- Single-model LLM summary mode with OpenAI-compatible API support
- Source health summary
- Benchmark, dataset, and GitHub project sections
- Evergreen classic paper recall section

## Quick Start

```bash
pip install -r requirements.txt
python run.py
```

Generated artifacts include:

- `report.md`
- `index.html`
- `reports/daily/latest.md`
- `reports/daily/YYYY/MM/YYYY-MM-DD.md`
- `data/raw/YYYY-MM-DD.jsonl`
- `data/processed/YYYY-MM-DD.json`

## GitHub Actions Setup

The scheduled workflow lives at `.github/workflows/daily-report.yml`. It runs
daily at 06:30 Asia/Shanghai and can also be started manually from:

GitHub -> Actions -> Daily AI Research Radar -> Run workflow

Configure production automation with GitHub Actions Secrets and Variables.
Do not commit API keys.

Secrets:

- `OPENAI_API_KEY`
- or fallback provider keys: `KIMI_API_KEY`, `DEEPSEEK_API_KEY`, `GLM_API_KEY`

Variables:

- `OPENAI_BASE_URL`
- `OPENAI_MODEL`
- optional provider variables: `KIMI_BASE_URL`, `KIMI_MODEL`, `DEEPSEEK_BASE_URL`, `DEEPSEEK_MODEL`, `GLM_BASE_URL`, `GLM_MODEL`

Recommended daily settings:

```env
MODEL_MODE=single
OPENAI_SUMMARY_BUDGET=3
MAX_OUTPUT_TOKENS=250
MAX_EVIDENCE_CHARS=1600
```

Recommended low-cost OpenAI-compatible provider example:

```env
OPENAI_BASE_URL=https://api.moonshot.cn/v1
OPENAI_MODEL=moonshot-v1-8k
```

## Cost Control

The default daily path is intentionally cost-safe:

- `MODEL_MODE=single`
- single-model summaries are capped by `OPENAI_SUMMARY_BUDGET`
- output length is capped by `MAX_OUTPUT_TOKENS`
- evidence length is capped by `MAX_EVIDENCE_CHARS`
- reports show Summary mode, Provider, Model, LLM summary calls, and Last LLM error

role_pipeline is kept only as an experimental advanced mode. It may call
DeepSeek, Kimi, GLM, or other role-specific models for one item and can multiply
API usage quickly. Do not enable it for the scheduled daily workflow unless the
higher cost is intentional.

## Current Limitations

- This release is a daily report generator MVP, not a full web application.
- Ranking still needs a feedback loop and may overweight Agent or video diffusion items.
- Context memory papers such as STALE / Q-RAG may need stronger promotion rules.
- GitHub awesome-list repositories may still be noisy.
- Some source parsers may fail silently or return 0 items.

## Release Notes

See `RELEASE_NOTES.md` for the v0.1.0 GitHub Release notes.
