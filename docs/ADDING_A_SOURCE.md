# Adding a Source

1. Decide whether the entry is only a registry entity or an active collector.
2. Add registry metadata to `associations.yaml`, `venues.yaml`,
   `organizations.yaml`, or `people.yaml`.
3. Add to `sources.yaml` only when the endpoint is stable.
4. Use `source_kind` and `source_role` honestly:
   - `primary` for papers, official blogs, and official pages.
   - `aggregator` for discovery and metadata services.
   - `media` for news or community context.
5. Add a mock-based fetcher test. Do not make default tests depend on the public
   internet.
