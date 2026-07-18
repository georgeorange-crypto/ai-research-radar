# Source Registry

v0.2 separates registries from collectors.

- `associations.yaml`: associations, awards, fellows, and leadership sources.
- `venues.yaml`: conferences, journals, transactions, magazines, proceedings.
- `organizations.yaml`: universities, institutes, labs, and companies.
- `people.yaml`: scholars and research leaders.
- `sources.yaml`: active collectors only.

Registry entries can be disabled or collector-free. Active sources must have a
fetcher in `fetch.py`, a timeout, update frequency, source role, and health
reporting. Discovery sources do not directly boost credibility.
