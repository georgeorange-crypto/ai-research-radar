from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Optional

import requests


RESPONSE_FORMAT_UNSTABLE_PROVIDERS = {"glm"}
AUTH_DISABLE_STATUS_CODES = {401, 402, 403}
CACHE_PATH = Path("data") / "llm_cache" / "global.json"
_LLM_CACHE: dict[str, Any] | None = None
LAST_MODEL_ERROR = ""
PROVIDER_DISABLED: dict[str, str] = {}
REQUEST_STATS = {
    "api_requests_total": 0,
    "api_requests_by_provider": Counter(),
    "api_requests_by_role": Counter(),
    "cache_hits": 0,
    "cache_misses": 0,
}


def _trim(text: str, limit: int = 500) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= limit:
        return text
    return text[:limit].rstrip()


def parse_json_object(content: str) -> Optional[dict[str, Any]]:
    """Parse provider JSON, including fenced ```json blocks."""
    text = (content or "").strip()
    fenced = re.search(r"```(?:json)?\s*(.*?)```", text, flags=re.IGNORECASE | re.DOTALL)
    if fenced:
        text = fenced.group(1).strip()

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start < 0 or end <= start:
            return None
        try:
            parsed = json.loads(text[start : end + 1])
        except json.JSONDecodeError:
            return None

    return parsed if isinstance(parsed, dict) else None


def log_model_error(provider: str, model: str, base_url: str, status: int | str | None, error_text: str) -> None:
    global LAST_MODEL_ERROR

    status_label = str(status) if status else "n/a"
    message = (
        f"provider={provider}; model={model}; base_url={base_url}; "
        f"HTTP status={status_label}; error={_trim(error_text, 500) or 'n/a'}"
    )
    LAST_MODEL_ERROR = message
    print(f"Model API error: {message}", file=sys.stderr, flush=True)


def _provider_key(provider: str) -> str:
    return (provider or "unknown").strip().lower()


def disable_reason(status: int | str | None, error_text: str) -> str:
    text = str(error_text or "").lower()
    try:
        status_int = int(status) if status is not None else None
    except (TypeError, ValueError):
        status_int = None
    if status_int == 402 or ("insufficient" in text and "balance" in text):
        return "insufficient_balance"
    if status_int == 401:
        return "unauthorized"
    if status_int == 403:
        return "forbidden"
    if status_int:
        return f"http_{status_int}"
    return "provider_error"


def disable_provider(provider: str, status: int | str | None, error_text: str) -> None:
    key = _provider_key(provider)
    reason = disable_reason(status, error_text)
    if key not in PROVIDER_DISABLED:
        PROVIDER_DISABLED[key] = reason
        print(f"Provider disabled for this run: provider={key}; reason={reason}", file=sys.stderr, flush=True)


def is_provider_disabled(provider: str) -> bool:
    return _provider_key(provider) in PROVIDER_DISABLED


def _record_api_request(provider: str, role: str) -> None:
    REQUEST_STATS["api_requests_total"] += 1
    REQUEST_STATS["api_requests_by_provider"][_provider_key(provider)] += 1
    REQUEST_STATS["api_requests_by_role"][role or "unknown"] += 1


def llm_stats_snapshot() -> dict[str, Any]:
    disabled = dict(PROVIDER_DISABLED)
    if len(disabled) == 1:
        disabled_reason = next(iter(disabled.values()))
    else:
        disabled_reason = ", ".join(f"{provider}:{reason}" for provider, reason in disabled.items()) or "none"
    try:
        from recommender.cost_guard import snapshot as cost_snapshot

        cost = cost_snapshot()
    except Exception:
        cost = {}
    return {
        "api_requests_total": int(REQUEST_STATS["api_requests_total"]),
        "api_requests_by_provider": dict(REQUEST_STATS["api_requests_by_provider"]),
        "api_requests_by_role": dict(REQUEST_STATS["api_requests_by_role"]),
        "cache_hits": int(REQUEST_STATS["cache_hits"]),
        "cache_misses": int(REQUEST_STATS["cache_misses"]),
        "last_model_error": LAST_MODEL_ERROR,
        "provider_disabled": ", ".join(disabled.keys()) or "none",
        "provider_disabled_reason": disabled_reason,
        "daily_llm_budget_rmb": cost.get("daily_budget_rmb"),
        "estimated_llm_cost_rmb": cost.get("estimated_rmb"),
        "estimated_input_tokens": cost.get("estimated_input_tokens"),
        "estimated_output_tokens": cost.get("estimated_output_tokens"),
        "cost_guard_blocked_calls": cost.get("blocked_calls"),
        "cost_guard_enabled": cost.get("enabled"),
    }


def _load_cache() -> dict[str, Any]:
    global _LLM_CACHE
    if _LLM_CACHE is not None:
        return _LLM_CACHE
    if not CACHE_PATH.exists():
        _LLM_CACHE = {}
        return _LLM_CACHE
    try:
        with open(CACHE_PATH, "r", encoding="utf-8") as f:
            parsed = json.load(f)
    except (OSError, ValueError):
        parsed = {}
    _LLM_CACHE = parsed if isinstance(parsed, dict) else {}
    return _LLM_CACHE


def _save_cache() -> None:
    if _LLM_CACHE is None:
        return
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(_LLM_CACHE, f, ensure_ascii=False, indent=2, sort_keys=True)


def make_llm_cache_key(provider: str, model: str, role: str, title: str, url: str, abstract_or_summary: str) -> str:
    raw = "\n".join(
        [
            _provider_key(provider),
            model or "",
            role or "",
            title or "",
            url or "",
            abstract_or_summary or "",
        ]
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def get_cached_json(cache_key: str | None) -> Optional[dict[str, Any]]:
    if not cache_key:
        return None
    cache = _load_cache()
    entry = cache.get(cache_key)
    if isinstance(entry, dict) and isinstance(entry.get("result"), dict):
        REQUEST_STATS["cache_hits"] += 1
        return entry["result"]
    if isinstance(entry, dict) and "result" not in entry:
        REQUEST_STATS["cache_hits"] += 1
        return entry
    REQUEST_STATS["cache_misses"] += 1
    return None


def store_cached_json(cache_key: str | None, result: dict[str, Any], metadata: dict[str, Any] | None = None) -> None:
    if not cache_key:
        return
    cache = _load_cache()
    cache[cache_key] = {
        "result": result,
        "metadata": metadata or {},
    }
    _save_cache()


def _unsupported_parameter_error(error_text: str, parameter: str) -> bool:
    text = (error_text or "").lower()
    return parameter.lower() in text and any(
        marker in text
        for marker in [
            "unsupported",
            "not support",
            "unrecognized",
            "unknown",
            "invalid",
            "not allowed",
            "extra_forbidden",
        ]
    )


class ChatModelClient:
    """Small OpenAI-compatible chat completions client with JSON fallback parsing."""

    def __init__(
        self,
        *,
        provider: str,
        api_key: str,
        base_url: str,
        model: str,
        timeout: float = 60,
    ) -> None:
        self.provider = provider or "unknown"
        self.api_key = api_key or ""
        self.base_url = (base_url or "").rstrip("/")
        self.model = model or ""
        self.timeout = timeout

    @property
    def configured(self) -> bool:
        return bool(self.api_key and self.base_url and self.model)

    @property
    def supports_response_format(self) -> bool:
        return self.provider.lower() not in RESPONSE_FORMAT_UNSTABLE_PROVIDERS

    def call_json(
        self,
        *,
        system_prompt: str,
        user_payload: dict[str, Any] | str,
        schema: dict[str, Any] | None = None,
        temperature: float = 0.2,
        timeout: float | None = None,
        max_tokens: int | None = None,
        role: str = "single",
        cache_key: str | None = None,
        required_fields: set[str] | None = None,
    ) -> Optional[dict[str, Any]]:
        cached = get_cached_json(cache_key)
        if cached is not None:
            if not required_fields or all(field in cached for field in required_fields):
                return cached

        if not self.configured:
            return None
        if is_provider_disabled(self.provider):
            return None

        if schema and isinstance(user_payload, dict):
            user_payload = {**user_payload, "required_json_schema": schema}
        user_content = user_payload if isinstance(user_payload, str) else json.dumps(user_payload, ensure_ascii=False)
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ]

        try:
            from recommender.cost_guard import max_output_tokens as guard_max_output_tokens

            effective_max_tokens = guard_max_output_tokens(max_tokens)
        except Exception:
            effective_max_tokens = max(1, min(250, int(max_tokens or 250)))

        attempts = [self.supports_response_format, False]
        seen: set[bool] = set()
        token_parameter = "max_tokens"
        for use_response_format in attempts:
            if use_response_format in seen:
                continue
            seen.add(use_response_format)

            while True:
                payload: dict[str, Any] = {
                    "model": self.model,
                    "messages": messages,
                    "temperature": temperature,
                }
                if token_parameter:
                    payload[token_parameter] = effective_max_tokens
                if use_response_format:
                    payload["response_format"] = {"type": "json_object"}

                try:
                    try:
                        from recommender.cost_guard import reserve_llm_call
                    except ModuleNotFoundError:
                        reserve_llm_call = None
                    except Exception as guard_exc:
                        log_model_error(self.provider, self.model, self.base_url, "budget_guard", str(guard_exc)[:500])
                        return None
                    if reserve_llm_call is not None:
                        reserve = reserve_llm_call(
                            provider=self.provider,
                            model=self.model,
                            role=role,
                            messages=messages,
                            max_tokens=effective_max_tokens,
                        )
                        if not reserve.allowed:
                            log_model_error(
                                self.provider,
                                self.model,
                                self.base_url,
                                "budget_guard",
                                (
                                    f"{reserve.reason}; budget_rmb={reserve.budget_rmb}; "
                                    f"spent_rmb={reserve.spent_rmb}; estimated_next_rmb={reserve.estimated_rmb}"
                                ),
                            )
                            return None
                    _record_api_request(self.provider, role)
                    response = requests.post(
                        f"{self.base_url}/chat/completions",
                        headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
                        json=payload,
                        timeout=timeout or self.timeout,
                    )
                except requests.RequestException as exc:
                    response = getattr(exc, "response", None)
                    status = getattr(response, "status_code", None)
                    error_text = getattr(response, "text", None) or str(exc)
                    log_model_error(self.provider, self.model, self.base_url, status, error_text)
                    try:
                        status_int = int(status) if status is not None else None
                    except (TypeError, ValueError):
                        status_int = None
                    if status_int in AUTH_DISABLE_STATUS_CODES:
                        disable_provider(self.provider, status_int, error_text)
                    return None

                if not response.ok:
                    error_text = response.text[:500]
                    log_model_error(self.provider, self.model, self.base_url, response.status_code, error_text)
                    if response.status_code in AUTH_DISABLE_STATUS_CODES:
                        disable_provider(self.provider, response.status_code, error_text)
                        return None
                    if token_parameter == "max_tokens" and _unsupported_parameter_error(error_text, "max_tokens"):
                        token_parameter = "max_completion_tokens"
                        continue
                    if use_response_format:
                        break
                    return None
                break

            if not response.ok:
                continue

            try:
                content = response.json()["choices"][0]["message"]["content"]
            except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
                log_model_error(self.provider, self.model, self.base_url, "n/a", str(exc)[:500])
                if use_response_format:
                    continue
                return None

            parsed = parse_json_object(content)
            if parsed is not None:
                if not required_fields or all(field in parsed for field in required_fields):
                    store_cached_json(
                        cache_key,
                        parsed,
                        {
                            "provider": self.provider,
                            "model": self.model,
                            "role": role,
                        },
                    )
                return parsed

            log_model_error(
                self.provider,
                self.model,
                self.base_url,
                "n/a",
                f"Could not parse JSON response: {content[:500]}",
            )
            if use_response_format:
                continue
            return None

        return None
