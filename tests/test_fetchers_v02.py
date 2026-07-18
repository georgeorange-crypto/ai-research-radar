from __future__ import annotations

from fetch import fetch_crossref_source, fetch_dblp_source, fetch_openalex_source, fetch_semantic_scholar_source


class Response:
    status_code = 200
    headers = {}
    text = "{}"
    ok = True

    def __init__(self, payload):
        self.payload = payload

    def json(self):
        return self.payload

    def raise_for_status(self):
        return None


class Http:
    def __init__(self, payload):
        self.payload = payload

    def get(self, *args, **kwargs):
        return Response(self.payload)


def test_metadata_fetchers_use_mock_responses() -> None:
    openalex = fetch_openalex_source({"id": "openalex", "name": "OpenAlex", "type": "openalex", "max_items": 1}, Http({"results": [{"display_name": "GPU Storage", "id": "W1", "publication_date": "2026-07-18", "primary_location": {"landing_page_url": "https://example.com/a"}}]}))
    crossref = fetch_crossref_source({"id": "crossref", "name": "Crossref", "type": "crossref", "max_items": 1}, Http({"message": {"items": [{"title": ["Checkpoint I/O"], "URL": "https://example.com/c", "issued": {"date-parts": [[2026]]}}]}}))
    semantic = fetch_semantic_scholar_source({"id": "semantic", "name": "Semantic", "type": "semantic_scholar", "max_items": 1}, Http({"data": [{"title": "Agent Runtime", "url": "https://example.com/s", "paperId": "S1"}]}))
    dblp = fetch_dblp_source({"id": "dblp", "name": "DBLP", "type": "dblp", "max_items": 1}, Http({"result": {"hits": {"hit": [{"info": {"title": "Distributed Systems", "ee": "https://example.com/d", "year": "2026"}}]}}}))
    assert openalex and crossref and semantic and dblp
