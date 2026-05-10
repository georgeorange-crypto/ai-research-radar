from __future__ import annotations

import argparse
import hashlib
import json
import logging
import re
import sys
import warnings
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urljoin, urlparse, urlunparse

import feedparser
import requests
import yaml
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
from dateutil import parser as date_parser

try:
    from ftfy import fix_text
except Exception:  # pragma: no cover
    def fix_text(text: str) -> str:
        return text


USER_AGENT = "ai-research-radar/0.1 (+https://github.com/your-name/ai-research-radar)"
DEFAULT_TIMEOUT = 25
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)


def configure_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def load_yaml(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data or {}


def normalize_space(value: Any) -> str:
    text = "" if value is None else str(value)
    text = fix_text(text)
    return re.sub(r"\s+", " ", BeautifulSoup(text, "html.parser").get_text(" ")).strip()


def get_nested_value(value: Any) -> Any:
    if isinstance(value, dict) and "value" in value:
        return value.get("value")
    return value


def parse_date(value: Any) -> str | None:
    if not value:
        return None
    if isinstance(value, (int, float)):
        # OpenReview uses milliseconds for tcdate/tmdate/pdate.
        seconds = value / 1000 if value > 10_000_000_000 else value
        return datetime.fromtimestamp(seconds, tz=timezone.utc).isoformat()
    try:
        parsed = date_parser.parse(str(value))
    except (ValueError, TypeError, OverflowError):
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).isoformat()


def openreview_forum_id_from_url(url: str) -> str | None:
    parsed = urlparse(url)
    if "openreview.net" not in parsed.netloc.lower():
        return None
    for value in parse_qs(parsed.query).get("id", []):
        forum_id = str(value).strip()
        if re.fullmatch(r"[A-Za-z0-9_-]{5,}", forum_id):
            return forum_id
    return None


def openreview_forum_url(forum_id: str) -> str:
    return f"https://openreview.net/forum?id={forum_id}"


def canonical_url(url: str, base_url: str | None = None) -> str:
    if not url:
        return ""
    if base_url:
        url = urljoin(base_url, url)
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return ""
    if "openreview.net" in parsed.netloc.lower():
        forum_id = openreview_forum_id_from_url(url)
        if forum_id:
            return openreview_forum_url(forum_id)
    parsed = parsed._replace(fragment="", query="")
    return urlunparse(parsed)


def make_id(title: str, url: str) -> str:
    raw = f"{title}|{url}".encode("utf-8", errors="ignore")
    return hashlib.sha256(raw).hexdigest()[:16]


def make_item(
    *,
    source: dict[str, Any],
    title: str,
    url: str,
    summary: str = "",
    published_at: str | None = None,
    authors: list[str] | None = None,
    tags: list[str] | None = None,
    metrics: dict[str, Any] | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    title = normalize_space(title)
    url = canonical_url(url, source.get("url"))
    if len(title) < 6 or not url:
        return None

    return {
        "id": make_id(title, url),
        "title": title,
        "url": url,
        "summary": normalize_space(summary),
        "published_at": published_at,
        "authors": authors or [],
        "tags": tags or [],
        "metrics": metrics or {},
        "metadata": metadata or {},
        "source": {
            "id": source.get("id"),
            "name": source.get("name"),
            "type": source.get("type"),
            "kind": source.get("source_kind", "primary"),
            "url": source.get("url"),
        },
    }


def session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT, "Accept": "*/*"})
    return s


def fetch_rss_source(source: dict[str, Any], http: requests.Session) -> list[dict[str, Any]]:
    response = http.get(source["url"], timeout=source.get("timeout", DEFAULT_TIMEOUT))
    response.raise_for_status()
    feed = feedparser.parse(response.content)
    items: list[dict[str, Any]] = []
    for entry in feed.entries[: source.get("max_items", 20)]:
        published = (
            getattr(entry, "published", None)
            or getattr(entry, "updated", None)
            or getattr(entry, "created", None)
        )
        authors = []
        for author in getattr(entry, "authors", []) or []:
            name = author.get("name") if isinstance(author, dict) else str(author)
            if name:
                authors.append(name)
        item = make_item(
            source=source,
            title=getattr(entry, "title", ""),
            url=getattr(entry, "link", ""),
            summary=getattr(entry, "summary", "") or getattr(entry, "description", ""),
            published_at=parse_date(published),
            authors=authors,
            tags=[tag.get("term") for tag in getattr(entry, "tags", []) if isinstance(tag, dict) and tag.get("term")],
        )
        if item:
            items.append(item)
    return items


def fetch_arxiv_source(source: dict[str, Any], http: requests.Session) -> list[dict[str, Any]]:
    categories = source.get("categories") or ["cs.AI"]
    query = " OR ".join(f"cat:{category}" for category in categories)
    params = {
        "search_query": query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": source.get("max_items", 100),
    }
    response = http.get("https://export.arxiv.org/api/query", params=params, timeout=source.get("timeout", DEFAULT_TIMEOUT))
    response.raise_for_status()
    feed = feedparser.parse(response.content)
    items: list[dict[str, Any]] = []
    for entry in feed.entries:
        authors = [a.get("name") for a in getattr(entry, "authors", []) if isinstance(a, dict) and a.get("name")]
        arxiv_id = getattr(entry, "id", "").rsplit("/", 1)[-1]
        abstract_url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else getattr(entry, "link", "")
        item = make_item(
            source=source,
            title=getattr(entry, "title", ""),
            url=abstract_url,
            summary=getattr(entry, "summary", ""),
            published_at=parse_date(getattr(entry, "published", None) or getattr(entry, "updated", None)),
            authors=authors,
            tags=[tag.get("term") for tag in getattr(entry, "tags", []) if isinstance(tag, dict) and tag.get("term")],
            metrics={"arxiv_id": arxiv_id},
        )
        if item:
            items.append(item)
    return items


def fetch_hf_daily_papers(source: dict[str, Any], http: requests.Session) -> list[dict[str, Any]]:
    response = http.get(source.get("api_url", "https://huggingface.co/api/daily_papers"), timeout=source.get("timeout", DEFAULT_TIMEOUT))
    response.raise_for_status()
    data = response.json()
    rows = data if isinstance(data, list) else data.get("papers", [])
    items: list[dict[str, Any]] = []
    for row in rows[: source.get("max_items", 40)]:
        paper = row.get("paper", row) if isinstance(row, dict) else {}
        paper_id = paper.get("id") or row.get("id")
        title = paper.get("title") or paper.get("paperTitle") or row.get("title")
        summary = paper.get("summary") or paper.get("abstract") or row.get("summary") or row.get("abstract") or ""
        authors = []
        for author in paper.get("authors", []) or row.get("authors", []) or []:
            if isinstance(author, dict):
                name = author.get("name") or author.get("fullname")
            else:
                name = str(author)
            if name:
                authors.append(name)
        url = paper.get("url") or row.get("url")
        if not url and paper_id:
            if re.match(r"^\d{4}\.\d{4,5}(v\d+)?$", str(paper_id)):
                url = f"https://arxiv.org/abs/{paper_id}"
            else:
                url = f"https://huggingface.co/papers/{paper_id}"
        item = make_item(
            source=source,
            title=title or "",
            url=url or source.get("url", ""),
            summary=summary,
            published_at=parse_date(row.get("publishedAt") or paper.get("publishedAt") or row.get("date")),
            authors=authors,
            tags=["huggingface-daily-papers"],
            metrics={
                "upvotes": row.get("upvotes") or paper.get("upvotes"),
                "paper_id": paper_id,
            },
        )
        if item:
            items.append(item)
    return items


def fetch_hf_papers_page(source: dict[str, Any], http: requests.Session) -> list[dict[str, Any]]:
    response = http.get(source["url"], timeout=source.get("timeout", DEFAULT_TIMEOUT))
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    items: list[dict[str, Any]] = []
    seen: set[str] = set()
    for link in soup.select('a[href^="/papers/"]'):
        href = link.get("href", "")
        match = re.match(r"^/papers/(\d{4}\.\d{4,5})(?:v\d+)?", href)
        if not match:
            continue
        paper_id = match.group(1)
        title = normalize_space(link.get_text(" ", strip=True))
        if len(title) < 8 or paper_id in seen:
            continue
        parent = link.find_parent(["article", "li"]) or link.find_parent("div")
        summary_node = parent.select_one("p") if parent and hasattr(parent, "select_one") else None
        item = make_item(
            source=source,
            title=title,
            url=f"https://arxiv.org/abs/{paper_id}",
            summary=summary_node.get_text(" ", strip=True) if summary_node else "",
            tags=["huggingface-trending-papers"],
            metrics={"paper_id": paper_id},
        )
        if item:
            seen.add(paper_id)
            items.append(item)
        if len(items) >= source.get("max_items", 30):
            break
    return items


def fetch_github_search_source(source: dict[str, Any], http: requests.Session) -> list[dict[str, Any]]:
    headers = {"Accept": "application/vnd.github+json"}
    token = source.get("token") or ""
    if token:
        headers["Authorization"] = f"Bearer {token}"

    items: list[dict[str, Any]] = []
    seen: set[str] = set()
    pushed_after_days = int(source.get("pushed_after_days", 365))
    pushed_after = (datetime.now(timezone.utc) - timedelta(days=pushed_after_days)).strftime("%Y-%m-%d")
    per_query = int(source.get("max_items_per_query", 5))

    def readme_excerpt(full_name: str) -> str:
        if not full_name:
            return ""
        readme_headers = {**headers, "Accept": "application/vnd.github.raw"}
        try:
            response = http.get(
                f"https://api.github.com/repos/{full_name}/readme",
                headers=readme_headers,
                timeout=source.get("timeout", DEFAULT_TIMEOUT),
            )
            if response.status_code != 200:
                return ""
            text = normalize_space(response.text)
            return text[:1800]
        except requests.RequestException:
            return ""

    for query in source.get("queries", []):
        q = str(query)
        if "pushed:" not in q:
            q = f"{q} pushed:>={pushed_after}"
        params = {
            "q": q,
            "sort": source.get("sort", "stars"),
            "order": source.get("order", "desc"),
            "per_page": per_query,
        }
        response = http.get("https://api.github.com/search/repositories", params=params, headers=headers, timeout=source.get("timeout", DEFAULT_TIMEOUT))
        if response.status_code == 403:
            logging.warning("GitHub API rate limit hit for query: %s", query)
            continue
        response.raise_for_status()
        for repo in response.json().get("items", [])[:per_query]:
            url = repo.get("html_url", "")
            if not url or url in seen:
                continue
            seen.add(url)
            topics = repo.get("topics") or []
            full_name = repo.get("full_name") or repo.get("name") or ""
            description = repo.get("description") or ""
            summary_bits = [
                description,
                f"Stars: {repo.get('stargazers_count', 0)}",
                f"Language: {repo.get('language') or 'Unknown'}",
            ]
            readme = readme_excerpt(full_name)
            item = make_item(
                source=source,
                title=full_name,
                url=url,
                summary=" | ".join(part for part in summary_bits if part),
                published_at=parse_date(repo.get("pushed_at") or repo.get("updated_at")),
                authors=[repo.get("owner", {}).get("login")] if repo.get("owner") else [],
                tags=["github", "open-source", *(str(topic) for topic in topics)],
                metrics={
                    "stars": repo.get("stargazers_count", 0),
                    "forks": repo.get("forks_count", 0),
                    "open_issues": repo.get("open_issues_count", 0),
                    "language": repo.get("language"),
                    "pushed_at": repo.get("pushed_at"),
                },
                metadata={
                    "github_description": description,
                    "repo_readme_summary": readme,
                    "topics": topics,
                },
            )
            if item:
                items.append(item)
            if len(items) >= source.get("max_items", 30):
                return items
    return items


def fetch_openreview_source(source: dict[str, Any], http: requests.Session) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    venue_ids = source.get("venue_ids") or []
    limit = source.get("max_items", 30)
    for venue_id in venue_ids:
        params = {
            "content.venueid": venue_id,
            "limit": limit,
            "sort": "tcdate:desc",
            "select": "id,forum,content.title,content.abstract,content.authors,content.venueid,tcdate,tmdate,pdate,odate",
        }
        response = http.get("https://api2.openreview.net/notes", params=params, timeout=source.get("timeout", DEFAULT_TIMEOUT))
        response.raise_for_status()
        for note in response.json().get("notes", [])[:limit]:
            content = note.get("content", {})
            title = normalize_space(get_nested_value(content.get("title")))
            abstract = normalize_space(get_nested_value(content.get("abstract")))
            raw_authors = get_nested_value(content.get("authors")) or []
            authors = raw_authors if isinstance(raw_authors, list) else []
            published = note.get("pdate") or note.get("odate") or note.get("tmdate") or note.get("tcdate")
            forum_id = str(note.get("forum") or note.get("id") or "").strip()
            item = make_item(
                source={**source, "name": f"{source.get('name')} ({venue_id})"},
                title=title,
                url=openreview_forum_url(forum_id) if forum_id else "https://openreview.net/forum",
                summary=abstract,
                published_at=parse_date(published),
                authors=[str(a) for a in authors],
                tags=["openreview", venue_id],
                metrics={"venue_id": venue_id, "openreview_forum_id": forum_id},
            )
            if item:
                items.append(item)
    return items


BAD_TITLES = {
    "home",
    "menu",
    "about",
    "contact",
    "privacy",
    "sponsor",
    "registration",
    "submit",
    "login",
    "sign in",
}


def extract_html_date(node: Any) -> str | None:
    time_node = node.select_one("time[datetime]") if hasattr(node, "select_one") else None
    if time_node:
        parsed = parse_date(time_node.get("datetime") or time_node.get_text(" "))
        if parsed:
            return parsed
    text = normalize_space(node.get_text(" ", strip=True) if hasattr(node, "get_text") else "")
    match = re.search(r"\b(20\d{2}[-/][01]?\d[-/][0-3]?\d|[A-Z][a-z]+ [0-3]?\d, 20\d{2})\b", text)
    return parse_date(match.group(1)) if match else None


def fetch_html_links_source(source: dict[str, Any], http: requests.Session) -> list[dict[str, Any]]:
    response = http.get(source["url"], timeout=source.get("timeout", DEFAULT_TIMEOUT))
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    selectors = source.get("selectors") or {}
    item_selector = selectors.get("item") or "article, li, .post, .entry"
    title_selector = selectors.get("title") or "h1, h2, h3, a"
    summary_selector = selectors.get("summary") or "p"

    nodes = soup.select(item_selector)
    if not nodes:
        nodes = soup.select("a")

    seen_urls: set[str] = set()
    items: list[dict[str, Any]] = []
    for node in nodes:
        title_node = node.select_one(title_selector) if hasattr(node, "select_one") else node
        link_node = title_node if getattr(title_node, "name", "") == "a" else node.select_one("a[href]")
        if not title_node or not link_node:
            continue
        title = normalize_space(title_node.get_text(" ", strip=True))
        if not title or title.lower() in BAD_TITLES or len(title) < 8:
            continue
        url = canonical_url(link_node.get("href", ""), source["url"])
        if not url or url in seen_urls:
            continue
        if urlparse(url).netloc == urlparse(source["url"]).netloc and urlparse(url).path in {"", "/"}:
            continue
        summary_node = node.select_one(summary_selector) if hasattr(node, "select_one") else None
        item = make_item(
            source=source,
            title=title,
            url=url,
            summary=summary_node.get_text(" ", strip=True) if summary_node else "",
            published_at=extract_html_date(node),
        )
        if item:
            seen_urls.add(url)
            items.append(item)
        if len(items) >= source.get("max_items", 20):
            break
    return items


FETCHERS = {
    "rss": fetch_rss_source,
    "arxiv": fetch_arxiv_source,
    "hf_daily_papers": fetch_hf_daily_papers,
    "hf_papers_page": fetch_hf_papers_page,
    "github_search": fetch_github_search_source,
    "openreview": fetch_openreview_source,
    "html_links": fetch_html_links_source,
}


def fetch_source(source: dict[str, Any], http: requests.Session) -> list[dict[str, Any]]:
    source_type = source.get("type")
    fetcher = FETCHERS.get(source_type)
    if not fetcher:
        logging.warning("Skip %s: unsupported type %s", source.get("id"), source_type)
        return []
    try:
        items = fetcher(source, http)
        logging.info("Fetched %s items from %s", len(items), source.get("name"))
        return items
    except Exception as exc:  # noqa: BLE001
        logging.warning("Fetch failed for %s: %s", source.get("name") or source.get("id"), exc)
        return []


def fetch_all(sources_path: str | Path = "config/sources.yaml") -> list[dict[str, Any]]:
    config = load_yaml(sources_path)
    http = session()
    items: list[dict[str, Any]] = []
    for source in config.get("sources", []):
        if source.get("enabled", True):
            items.extend(fetch_source(source, http))
    fetched_at = datetime.now(timezone.utc).isoformat()
    for item in items:
        item["fetched_at"] = fetched_at
    return items


def save_json(path: str | Path, payload: Any) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def save_jsonl(path: str | Path, rows: list[dict[str, Any]]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False))
            f.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch AI research radar sources.")
    parser.add_argument("--sources", default="config/sources.yaml")
    parser.add_argument("--output", default="data/raw.json")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    configure_logging(args.verbose)
    items = fetch_all(args.sources)
    save_json(args.output, items)
    print(f"wrote {len(items)} items to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
