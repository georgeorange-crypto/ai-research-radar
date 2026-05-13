from __future__ import annotations

import json
import re
import sys
from typing import Any, Optional

import requests


RESPONSE_FORMAT_UNSTABLE_PROVIDERS = {"glm"}


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
    status_label = str(status) if status else "n/a"
    message = (
        f"provider={provider}; model={model}; base_url={base_url}; "
        f"HTTP status={status_label}; error={_trim(error_text, 500) or 'n/a'}"
    )
    print(f"Model API error: {message}", file=sys.stderr, flush=True)


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
    ) -> Optional[dict[str, Any]]:
        if not self.configured:
            return None

        if schema and isinstance(user_payload, dict):
            user_payload = {**user_payload, "required_json_schema": schema}
        user_content = user_payload if isinstance(user_payload, str) else json.dumps(user_payload, ensure_ascii=False)
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ]

        attempts = [self.supports_response_format, False]
        seen: set[bool] = set()
        for use_response_format in attempts:
            if use_response_format in seen:
                continue
            seen.add(use_response_format)

            payload: dict[str, Any] = {
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
            }
            if use_response_format:
                payload["response_format"] = {"type": "json_object"}

            try:
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
                return None

            if not response.ok:
                log_model_error(self.provider, self.model, self.base_url, response.status_code, response.text[:500])
                if use_response_format:
                    continue
                return None

            try:
                content = response.json()["choices"][0]["message"]["content"]
            except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
                log_model_error(self.provider, self.model, self.base_url, "n/a", str(exc)[:500])
                if use_response_format:
                    continue
                return None

            parsed = parse_json_object(content)
            if parsed is not None:
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
