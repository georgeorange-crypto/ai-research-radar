# Research Profile

`config/research_profile.yaml` is the single source of truth for George Research
Profile v2. It defines the five P0 tracks, active projects, project relevance
terms, context gates, negative contexts, and MUST_READ buckets.

When adding or changing research direction:

- Add the term to the relevant track as `strong_terms` only if it is specific.
- Put ambiguous words such as `agent`, `systems`, `memory`, `compression`, and
  `world model` in `supporting_terms` plus a context gate.
- Add project terms under `projects` when they map to SkyFS, SchedAgent, VeRL
  infrastructure, or embodied intelligence.
- Keep legacy sections in `config/keywords.yaml`; do not delete old terms.
