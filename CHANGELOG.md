# Changelog

## v0.1.0 - 2026-05-18

### Added
- Daily AI research radar generation
- Multi-source AI research collection
- Daily Markdown report
- GitHub Pages HTML report
- Source health summary
- Single-model LLM summary mode
- OpenAI-compatible API support
- Research-focused ranking for LLM agents, context compression, RL, open-world learning, and model distillation
- Benchmark / dataset / GitHub project sections
- Evergreen classic paper recall section

### Changed
- Default mode is now single
- role_pipeline is kept as an experimental advanced mode, not default

### Fixed
- Avoid default multi-model role pipeline cost explosion
- Show summary mode, provider, model, LLM calls, and last error in reports

### Known Issues
- Ranking still sometimes overweights Agent / video diffusion items
- Context memory papers such as STALE / Q-RAG may need stronger promotion rules
- GitHub awesome-list repositories may still be noisy
- Meta AI Blog parser may return 0 items
- Web app / interactive dashboard not included in this release
