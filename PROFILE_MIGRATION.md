# Profile Migration Notes

v0.2 is additive. It keeps existing source ids, keywords, sections, reports,
single-model mode, and role-pipeline mode.

Major migration points:

- New P0 tracks are defined in `config/research_profile.yaml`.
- Legacy primary sections remain as supporting tracks.
- MUST_READ buckets are now Systems, GPU I/O, Compression, Agent/RL Infra, and
  Embodied World Models.
- `.env` is ignored and should stay local. Use `.env.example` and GitHub
  Secrets/Variables for deployment.
- Processed JSON now includes `track_relevance`, `project_relevance`,
  `source_provenance`, `feedback_score`, and `topic_drift_risk` with defaults.
