from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import yaml
from dotenv import dotenv_values, load_dotenv
from jinja2 import Environment, FileSystemLoader

from md_to_html import archive_report_with_timestamp, generate_html_report

# 加载 .env 环境变量
DOTENV_PATH = Path(".env")
DOTENV_VALUES = dotenv_values(DOTENV_PATH) if DOTENV_PATH.exists() else {}
load_dotenv(override=False)

if (
    os.getenv("GITHUB_ACTIONS") == "true"
    and "OPENAI_API_KEY" in os.environ
    and not os.environ.get("OPENAI_API_KEY")
    and DOTENV_VALUES.get("OPENAI_API_KEY")
):
    print(
        "Warning: .env contains OPENAI_API_KEY, but GitHub Actions provided OPENAI_API_KEY as an empty string; "
        "using the .env fallback for LLM config.",
        file=sys.stderr,
        flush=True,
    )

LLM_SUMMARY_CALLS = 0
LAST_LLM_ERROR = ""
MULTI_MODEL_INSTANCE = None
MULTI_MODEL_MODE = ""
LLM_ITEMS_PROCESSED = 0
ROLE_PIPELINE_ITEMS = 0
SINGLE_LLM_ITEMS = 0
ROLE_PIPELINE_ALLOWED_KEYS: set[str] = set()
SINGLE_LLM_ALLOWED_KEYS: set[str] = set()
LLM_PLAN_READY = False


KIND_LABELS = {
    "primary": "一手来源",
    "aggregator": "聚合/摘要",
    "media": "媒体摘要",
}

GROUP_LABELS = {
    "core_focus": "重点研究方向",
    "primary_research": "重点研究方向",
    "traditional_ai": "传统 AI 基础领域",
    "traditional_fields": "传统 AI 基础领域",
    "other": "Other Highlights",
}

TIER_LABELS = {
    "MUST_READ": "MUST_READ",
    "SKIM": "SKIM",
    "WATCH": "WATCH",
    "ARCHIVE": "ARCHIVE",
    "IGNORE": "IGNORE",
    "clone_and_run": "clone_and_run",
    "study_code": "study_code",
    "use_as_baseline": "use_as_baseline",
    "read_readme": "read_readme",
    "save": "save",
    "archive": "archive",
}

SUMMARY_FIELDS = [
    "what_is_it",
    "problem",
    "method_or_contribution",
    "why_important",
    "deep_read",
    "suggested_action",
]

ACTION_CHOICES = {
    "read_pdf",
    "skim",
    "watch",
    "save",
    "ignore",
    "use_as_eval",
    "clone_and_run",
    "study_code",
    "use_as_baseline",
    "read_readme",
    "archive",
}

OPEN_SOURCE_ACTIONS = {"study_code", "use_as_baseline", "clone_and_run", "read_readme", "save", "archive"}

DEFAULT_TEMPLATE_PATH = Path("config") / "daily_report.md.j2"

SECTION_DISPLAY_NAMES = {
    "context_compression_memory": "上下文压缩 / 长上下文 / 记忆",
    "context_compression": "上下文压缩 / 长上下文 / 记忆",
    "context_memory": "上下文压缩 / 长上下文 / 记忆",
    "agents": "Agent / Reasoning / Inference-time Scaling / Planning",
    "open_world_learning": "新类学习 / 开放世界学习",
    "open_world": "新类学习 / 开放世界学习",
    "model_distillation": "模型蒸馏 / 模型压缩",
    "distillation_efficiency": "模型蒸馏 / 模型压缩",
    "cv": "CV",
    "nlp": "NLP",
    "rl": "RL",
    "model_architecture": "模型架构",
    "architecture": "模型架构",
    "learning_methods": "学习方法",
    "highlights": "其他方向最耀眼成果",
    "other_highlights": "其他方向最耀眼成果",
    "benchmark_evaluation": "Benchmark / Dataset / Evaluation",
    "github_projects": "GitHub / 开源项目推荐",
    "institutional_updates": "企业 / 大学 / 研究所动态",
}


def load_json(path: str | Path) -> Any:
    with open(path, "r", encoding="utf-8-sig") as f:
        return json.load(f)


def trim(text: str, limit: int = 360) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def getenv_nonempty(name: str, default: str = "") -> str:
    return os.getenv(name) or default


def dotenv_nonempty(name: str, default: str = "") -> str:
    value = DOTENV_VALUES.get(name)
    if value is None:
        return default
    return str(value) or default


def config_env(name: str, default: str = "") -> str:
    return getenv_nonempty(name, dotenv_nonempty(name, default))


def config_bool(name: str, default: bool = False) -> bool:
    value = config_env(name)
    if not value:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def config_int(name: str, default: int, *, minimum: int = 0) -> int:
    try:
        return max(minimum, int(config_env(name, str(default))))
    except (TypeError, ValueError):
        return default


def infer_provider_from_openai_config(base_url: str, model: str) -> str:
    override = config_env("OPENAI_PROVIDER")
    if override:
        return override.strip().lower()
    text = f"{base_url} {model}".lower()
    if "moonshot" in text or "kimi" in text:
        return "kimi"
    if "deepseek" in text:
        return "deepseek"
    if "bigmodel" in text or "glm" in text or "zhipu" in text:
        return "glm"
    if "openai.com" in text:
        return "openai"
    return "openai-compatible"


def get_single_llm_config() -> dict[str, str]:
    openai_api_key = config_env("OPENAI_API_KEY")
    if openai_api_key:
        base_url = (config_env("OPENAI_BASE_URL") or "https://api.openai.com/v1").rstrip("/")
        model = config_env("OPENAI_MODEL", "gpt-4o-mini")
        return {
            "provider": infer_provider_from_openai_config(base_url, model),
            "api_key": openai_api_key,
            "base_url": base_url,
            "model": model,
        }

    deepseek_api_key = config_env("DEEPSEEK_API_KEY")
    if deepseek_api_key:
        return {
            "provider": "deepseek",
            "api_key": deepseek_api_key,
            "base_url": (config_env("DEEPSEEK_BASE_URL") or "https://api.deepseek.com").rstrip("/"),
            "model": config_env("DEEPSEEK_MODEL", "deepseek-v4-flash"),
        }

    kimi_api_key = config_env("KIMI_API_KEY")
    if kimi_api_key:
        return {
            "provider": "kimi",
            "api_key": kimi_api_key,
            "base_url": (config_env("KIMI_BASE_URL") or "https://api.moonshot.cn/v1").rstrip("/"),
            "model": config_env("KIMI_MODEL", "moonshot-v1-8k"),
        }

    glm_api_key = config_env("GLM_API_KEY")
    if glm_api_key:
        return {
            "provider": "glm",
            "api_key": glm_api_key,
            "base_url": (config_env("GLM_BASE_URL") or "https://open.bigmodel.cn/api/paas/v4").rstrip("/"),
            "model": config_env("GLM_MODEL", "glm-4.7-flash"),
        }

    return {
        "provider": "local",
        "api_key": "",
        "base_url": "",
        "model": "local fallback",
    }


def has_any_llm_api_key() -> bool:
    return bool(get_single_llm_config().get("api_key"))


def configured_model_mode(config: dict[str, Any] | None = None) -> str:
    if config is None:
        config = load_model_config()
    env_mode = config_env("MODEL_MODE")
    if env_mode:
        return env_mode.strip()
    config_mode = str(config.get("mode") or "").strip()
    if config_mode:
        if config_mode in {"role_pipeline", "ensemble"}:
            return "single"
        return config_mode
    return "single"


def ensemble_enabled() -> bool:
    return configured_model_mode() in {"ensemble", "role_pipeline"}


def _replace_env_var(value: str) -> str:
    """替换字符串中的环境变量引用 ${VAR_NAME}"""
    if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
        env_var = value[2:-1]
        return config_env(env_var, "")
    return value


def _replace_model_env_values(mapping: dict[str, Any], keys: list[str]) -> None:
    for key in keys:
        if key in mapping:
            mapping[key] = _replace_env_var(mapping[key])


def load_model_config() -> dict[str, Any]:
    config_path = Path("config") / "models.yaml"
    if not config_path.exists():
        return {}
    
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}
    
    configured_models = []
    for model in config.get("models", []) or []:
        _replace_model_env_values(model, ["api_key", "base_url", "model"])
        if model.get("api_key"):
            configured_models.append(model)
    if "models" in config:
        config["models"] = configured_models

    roles = config.get("roles", {})
    if isinstance(roles, dict):
        for role_config in roles.values():
            if isinstance(role_config, dict):
                _replace_model_env_values(role_config, ["api_key", "base_url", "model"])
    
    editor_config = config.get("editor", {})
    for key in ["api_key", "base_url", "model"]:
        if key in editor_config:
            editor_config[key] = _replace_env_var(editor_config[key])
    
    return config


def get_ensemble_model():
    global MULTI_MODEL_INSTANCE, MULTI_MODEL_MODE

    config = load_model_config()
    mode = configured_model_mode(config)
    if MULTI_MODEL_INSTANCE is not None and MULTI_MODEL_MODE == mode:
        return MULTI_MODEL_INSTANCE

    try:
        if mode == "role_pipeline":
            from models.role_pipeline import RolePipeline

            model = RolePipeline(config)
            if not model.available:
                return None
        elif mode == "ensemble":
            from models.ensemble import EnsembleModel

            model = EnsembleModel(config)
        else:
            return None
        MULTI_MODEL_INSTANCE = model
        MULTI_MODEL_MODE = mode
        return model
    except ImportError:
        return None


def role_pipeline_configured(config: dict[str, Any]) -> bool:
    roles = config.get("roles", {})
    if not isinstance(roles, dict):
        return False
    critic_llm_enabled = config_bool("CRITIC_LLM_ENABLED", bool(config.get("critic_llm_enabled", False)))
    rule_based_critic = config_bool("RULE_BASED_CRITIC", bool(config.get("rule_based_critic", True)))
    required = ["technical_extractor", "relevance_judge", "editor"]
    if critic_llm_enabled and not rule_based_critic:
        required.append("critic")
    return all(
        isinstance(roles.get(role), dict)
        and roles[role].get("api_key")
        and roles[role].get("base_url")
        and roles[role].get("model")
        for role in required
    )


def role_summary_lines(config: dict[str, Any]) -> str:
    roles = config.get("roles", {})
    if not isinstance(roles, dict):
        return ""
    critic_llm_enabled = config_bool("CRITIC_LLM_ENABLED", bool(config.get("critic_llm_enabled", False)))
    rule_based_critic = config_bool("RULE_BASED_CRITIC", bool(config.get("rule_based_critic", True)))
    labels = {
        "technical_extractor": "technical_extractor",
        "relevance_judge": "relevance_judge",
        "critic": "critic",
        "editor": "editor",
    }
    lines = []
    for role, label in labels.items():
        role_config = roles.get(role, {})
        if role == "critic" and (not critic_llm_enabled or rule_based_critic):
            lines.append("- critic: rule_based (deterministic)")
            continue
        if not isinstance(role_config, dict):
            continue
        provider = role_config.get("provider") or role_config.get("type") or "unconfigured"
        model = role_config.get("model") or "unconfigured"
        suffix = "" if role_config.get("api_key") else " (missing api_key)"
        lines.append(f"- {label}: {model} ({provider}){suffix}")
    return "\n".join(lines)


def active_summary_backend() -> dict[str, str]:
    config = load_model_config()
    mode = configured_model_mode(config)
    single_config = get_single_llm_config()
    if mode == "local":
        return {
            "summary_mode": "local",
            "provider": "local",
            "model": "local fallback",
            "roles": "",
        }
    if mode == "role_pipeline" and role_pipeline_configured(config):
        return {
            "summary_mode": "role_pipeline",
            "provider": "role_pipeline",
            "model": "role-based multi-model",
            "roles": role_summary_lines(config),
        }
    if mode == "ensemble" and config.get("models"):
        names = [f"{m.get('type') or m.get('provider')}:{m.get('model')}" for m in config.get("models", [])]
        return {
            "summary_mode": "ensemble",
            "provider": "ensemble",
            "model": ", ".join(names) or "ensemble",
            "roles": "",
        }
    if single_config.get("api_key"):
        return {
            "summary_mode": "single",
            "provider": single_config.get("provider", "local"),
            "model": single_config.get("model", "local fallback"),
            "roles": "",
        }
    return {
        "summary_mode": mode if mode == "single" else "local",
        "provider": "local",
        "model": "local fallback",
        "roles": "",
    }


def openai_timeout_seconds() -> float:
    return float(config_env("OPENAI_TIMEOUT_SECONDS", "20"))


def openai_summary_budget() -> int:
    return config_int("OPENAI_SUMMARY_BUDGET", 3, minimum=0)


def max_llm_items() -> int:
    return config_int("MAX_LLM_ITEMS", 5, minimum=0)


def single_llm_budget() -> int:
    return config_int("SINGLE_LLM_BUDGET", openai_summary_budget(), minimum=0)


def role_pipeline_budget() -> int:
    return config_int("ROLE_PIPELINE_BUDGET", 3, minimum=0)


def max_evidence_chars() -> int:
    return config_int("MAX_EVIDENCE_CHARS", 1600, minimum=1)


def max_output_tokens() -> int:
    return config_int("MAX_OUTPUT_TOKENS", 250, minimum=1)


GROUNDING_LABELS = {
    "title_only": "title only",
    "abstract_only": "abstract only",
    "full_text": "full text",
    "repo_readme": "repo README",
}


def metadata_dict(item: dict[str, Any]) -> dict[str, Any]:
    metadata = item.get("metadata")
    return metadata if isinstance(metadata, dict) else {}


def repo_readme_summary(item: dict[str, Any]) -> str:
    metadata = metadata_dict(item)
    for key in ["repo_readme_summary", "readme_summary", "readme_excerpt"]:
        value = metadata.get(key)
        if value:
            return str(value)
    return ""


def is_repository_item(item: dict[str, Any]) -> bool:
    tier = str(item.get("reading_tier", ""))
    source_type = item.get("source", {}).get("type")
    return bool(item.get("is_repository_item") or item.get("is_open_source_project") or source_type == "github_search" or tier in {"clone_and_run", "study_code", "use_as_baseline", "read_readme", "save", "archive"})


def grounding_level(item: dict[str, Any]) -> str:
    existing = str(item.get("grounding_level") or "").strip()
    if existing in GROUNDING_LABELS:
        return existing
    if is_repository_item(item):
        return "repo_readme" if repo_readme_summary(item) else "title_only"
    summary = str(item.get("abstract") or item.get("summary") or "").strip()
    if not summary:
        return "title_only"
    source_type = str(item.get("source", {}).get("type", "")).lower()
    if source_type in {"arxiv", "openreview", "hf_daily_papers", "hf_papers_page"}:
        return "abstract_only"
    return "full_text"


def grounding_label(item: dict[str, Any]) -> str:
    return GROUNDING_LABELS.get(grounding_level(item), "abstract only")


def allowed_evidence_text(item: dict[str, Any]) -> str:
    pieces = [
        str(item.get("title", "")),
        str(item.get("abstract") or item.get("summary") or ""),
        json.dumps(item.get("source", {}), ensure_ascii=False),
        str(item.get("url", "")),
        json.dumps(metadata_dict(item), ensure_ascii=False),
        repo_readme_summary(item),
    ]
    return "\n".join(piece for piece in pieces if piece.strip())


def is_benchmark_item(item: dict[str, Any]) -> bool:
    return item.get("primary_section", {}).get("id") == "benchmark_evaluation" or item.get("primary_category", {}).get("id") == "benchmark_evaluation"


def benchmark_action(item: dict[str, Any]) -> str:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    if any(term in text for term in ["agent", "workflow", "planning", "long-horizon", "long horizon", "memory", "safety"]):
        return "use_as_eval"
    if any(term in text for term in ["medical", "epidemic", "video", "domain generalization"]):
        return "save"
    if any(term in text for term in ["benchmark", "dataset", "evaluation"]):
        return "skim"
    return "ignore"


def apply_action_constraints(action: str, item: dict[str, Any]) -> str:
    """
    应用 suggested_action 的硬约束：
    
    1. MUST_READ -> read_pdf
    2. SKIM -> skim
    3. WATCH -> watch 或 save
    4. ARCHIVE -> archive 或 save
    5. 如果 is_open_source_project=true，则 suggested_action 只能是：
       study_code / clone_and_run / read_readme / save / archive
    6. 如果 grounding_level=title_only，则 suggested_action 不得为 read_pdf
    7. 如果 primary_category 是 GitHub / Open Source Projects，则不得进入今日深读清单
    8. Benchmark 如果值得用作实验，增加 secondary_action: use_as_eval
    """
    tier = item.get("reading_tier", "").upper()
    is_open_source = item.get("is_open_source_project", False)
    ground_level = grounding_level(item)
    explicit_override = item.get("explicit_override", False)
    
    if action == "read_pdf":
        if tier == "WATCH":
            return "watch"
        if tier == "ARCHIVE":
            return "archive"
        if tier == "SKIM" and not explicit_override:
            return "skim"
        if is_open_source:
            return "read_readme"
        if ground_level == "title_only":
            return "save"
        
        section_title = item.get("primary_category", {}).get("title", "")
        if section_title == "GitHub / Open Source Projects":
            return "read_readme"
    
    if is_open_source:
        if action in {"study_code", "clone_and_run", "read_readme", "save", "archive"}:
            return action
        return "read_readme"
    
    return action


def choose_action(item: dict[str, Any]) -> str:
    tier = item.get("reading_tier", "ARCHIVE")
    scores = item.get("scores", {})
    if is_repository_item(item):
        action = item.get("github_action") or tier if tier in ACTION_CHOICES else "read_readme"
        return apply_action_constraints(action, item)
    if is_benchmark_item(item):
        action = item.get("benchmark_action") or benchmark_action(item)
        if action == "use_as_eval":
            item["secondary_action"] = "use_as_eval"
        return apply_action_constraints(action, item)
    if tier == "IGNORE":
        return "ignore"
    if tier == "MUST_READ":
        return apply_action_constraints("read_pdf", item)
    if tier == "SKIM":
        return apply_action_constraints("skim", item)
    if tier == "WATCH":
        return apply_action_constraints("watch", item)
    if tier == "ARCHIVE":
        return apply_action_constraints("archive", item)
    return apply_action_constraints("save", item)


def normalize_action(value: Any, item: dict[str, Any]) -> str:
    action = str(value or "").strip().lower()
    if action in ACTION_CHOICES:
        return apply_action_constraints(action, item)
    return choose_action(item)


def normalize_summary(payload: dict[str, Any] | None, item: dict[str, Any]) -> dict[str, str]:
    fallback = fallback_summary(item)
    if not isinstance(payload, dict):
        return fallback

    normalized: dict[str, str] = {}
    for field in SUMMARY_FIELDS:
        value = str(payload.get(field, "")).strip()
        normalized[field] = value or fallback[field]
    if grounding_level(item) == "full_text" and "核心信号" in " ".join(normalized.values()):
        normalized = full_text_fallback_summary(item)
    normalized["suggested_action"] = normalize_action(normalized["suggested_action"], item)
    return normalized


def salient_terms(item: dict[str, Any], limit: int = 5) -> list[str]:
    terms: list[str] = []
    for term in item.get("matched_keywords", []):
        text = str(term).strip()
        if text and text.lower() not in {"benchmark", "dataset", "evaluation", "paper", "method"}:
            terms.append(text)
    evidence = f"{item.get('title', '')} {item.get('summary', '')}"
    for token in re.findall(r"\b[A-Z][A-Za-z0-9]*(?:[-_][A-Za-z0-9]+)*\b", evidence):
        if len(token) >= 3 and token not in terms:
            terms.append(token)
    return terms[:limit]


def item_kind_cn(item: dict[str, Any]) -> str:
    if is_repository_item(item):
        return "开源项目"
    if is_benchmark_item(item):
        return "评测基准或数据集论文"
    source_type = str(item.get("source", {}).get("type", "")).lower()
    if source_type in {"arxiv", "openreview", "hf_daily_papers", "hf_papers_page"}:
        return "研究论文"
    return "研究动态"


def contribution_hint_cn(item: dict[str, Any], names: list[str]) -> str:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    name_text = "、".join(names[:4])
    if is_repository_item(item):
        return "这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。"
    if any(word in text for word in ["introduce", "introduces", "present", "presents", "propose", "proposes"]):
        if name_text:
            return f"摘要可确认它提出或引入了 {name_text}；具体训练设置、指标和消融细节需读原文确认。"
        return "摘要可确认它提出了新的方法、数据或评测设定；方法细节未在摘要中充分展开。"
    if any(word in text for word in ["benchmark", "dataset", "evaluation", "evaluate"]):
        return "摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。"
    return "方法细节未在摘要中充分展开，细节需读原文确认。"


def full_text_fallback_summary(item: dict[str, Any]) -> dict[str, Any]:
    title = item.get("title") or "未命名条目"
    section = item.get("primary_category", item.get("primary_section", {})).get("title", "相关方向")
    summary = trim(str(item.get("summary") or item.get("abstract") or ""), 520)
    scores = item.get("scores", {})
    tier = item.get("reading_tier", "ARCHIVE")
    lower_title = str(title).lower()

    if "adaptive parallel reasoning" in lower_title:
        what_is_it = "Adaptive Parallel Reasoning 讨论如何把推理时计算从单一路径扩展为多条并行候选路径，并在搜索、验证或聚合后得到更稳的答案。"
        problem = "它针对的是复杂问题中串行 chain-of-thought 容易早早走偏、单次采样难以覆盖多种解法的问题。"
        method = "方法范式是 inference-time scaling：并行生成多个推理分支，再用选择、交叉检查或自适应预算分配把计算集中到更有希望的路径上。"
        importance = "这类工作直接关系到 agent planning、长上下文任务和测试时计算分配，说明提升推理能力不只依赖更大模型，也依赖更好的推理组织方式。"
    else:
        lead = summary or f"该条目来自 full text source，主题是 {title}。"
        what_is_it = f"{title} 是一篇围绕 {section} 的研究或技术文章；从正文摘要看，重点是：{lead}"
        problem = f"它关注 {section} 中尚未被充分解决的建模、推理、系统或评测问题，具体问题线索来自原文正文而不是标题关键词。"
        method = "它的贡献需要按正文脉络理解：先界定问题，再给出方法、系统设计、实验观察或研究范式，而不是只用关键词归类。"
        importance = f"该来源具备 full text grounding，适合用作当天判断 {section} 方向变化的实质材料；personal={scores.get('personal_score', 0):.2f}, relevance={scores.get('research_relevance', 0):.2f}。"

    action = choose_action(item)
    if tier == "MUST_READ":
        deep_read = "建议今天深读，重点看问题设定、方法范式和实验是否能迁移到自己的研究主线。"
    elif tier == "SKIM":
        deep_read = "建议略读正文，先抓住问题定义和方法框架。"
    else:
        deep_read = "今天不必深读，但建议保留为后续方向判断的背景材料。"

    return {
        "what_is_it": what_is_it,
        "problem": problem,
        "method_or_contribution": method,
        "why_important": importance,
        "deep_read": deep_read,
        "suggested_action": action,
    }


def fallback_summary(item: dict[str, Any]) -> dict[str, Any]:
    if grounding_level(item) == "full_text" and not is_repository_item(item):
        return full_text_fallback_summary(item)

    section = item.get("primary_category", item.get("primary_section", {})).get("title", "相关方向")
    tier = item.get("reading_tier", "ARCHIVE")
    scores = item.get("scores", {})
    names = salient_terms(item)
    keywords = "、".join(names[:4])
    title = item.get("title") or "未命名条目"

    if grounding_level(item) == "title_only":
        what_is_it = f"从标题可判断，这是关于“{title}”的{item_kind_cn(item)}，目前缺少摘要支撑。"
    else:
        focus = f"；主要线索：{keywords}" if keywords else ""
        what_is_it = f"{title}：{item_kind_cn(item)}，方向为“{section}”{focus}。"

    if keywords:
        problem = f"它关注“{section}”里的 {keywords} 等问题。"
    else:
        problem = f"它与“{section}”相关，但摘要中的问题表述不够具体。"

    method_or_contribution = contribution_hint_cn(item, names)

    importance_parts = [f"tier={tier}", f"editorial_priority={item.get('editorial_priority', 0):.2f}"]
    if tier == "MUST_READ":
        importance_parts.append("今天安排深读。")
    elif tier == "SKIM":
        importance_parts.append("今天快速扫读。")
    elif tier == "WATCH":
        importance_parts.append("方向相关，先追踪不深读。")
    elif tier == "ARCHIVE":
        importance_parts.append("归档备用。")
    elif tier in ACTION_CHOICES:
        importance_parts.append("按 GitHub 项目动作处理。")
    else:
        importance_parts.append("不进入正文阅读队列。")

    importance_parts.append(f"personal={scores.get('personal_score', 0):.2f}，relevance={scores.get('research_relevance', 0):.2f}。")

    action = choose_action(item)
    deep_read = "建议今天深读。" if action == "read_pdf" else "今天不深读，先按行动建议处理。"
    if tier == "IGNORE":
        deep_read = "不建议深读。"

    return {
        "what_is_it": what_is_it,
        "problem": problem,
        "method_or_contribution": method_or_contribution,
        "why_important": " ".join(importance_parts),
        "deep_read": deep_read,
        "suggested_action": action,
    }


def record_llm_error(provider: str, model: str, base_url: str, status: int | str | None, error_text: str) -> None:
    global LAST_LLM_ERROR

    status_label = str(status) if status else "n/a"
    snippet = trim(error_text or "", 500)
    LAST_LLM_ERROR = (
        f"provider={provider}; model={model}; base_url={base_url}; "
        f"HTTP status={status_label}; error={snippet or 'n/a'}"
    )
    print(f"LLM API error: {LAST_LLM_ERROR}", file=sys.stderr, flush=True)


def summarize_with_single_llm(item: dict[str, Any]) -> dict[str, Any] | None:
    config = get_single_llm_config()
    api_key = config.get("api_key", "")
    if not api_key:
        return None

    provider = config.get("provider", "openai")
    base_url = config.get("base_url", "").rstrip("/")
    model = config.get("model", "gpt-4o-mini")
    if grounding_level(item) == "title_only":
        return None
    evidence = trim(allowed_evidence_text(item), max_evidence_chars())
    prompt = {
        "title": item.get("title"),
        "source": item.get("source", {}),
        "url": item.get("url"),
        "metadata": metadata_dict(item),
        "repo_readme_summary": repo_readme_summary(item),
        "allowed_evidence": evidence,
        "grounding_level": grounding_level(item),
        "primary_section": item.get("primary_section", {}),
        "secondary_tags": item.get("secondary_tags", []),
        "reading_tier": item.get("reading_tier"),
        "matched_focus_areas": item.get("matched_focus_areas", []),
        "matched_keywords": item.get("matched_keywords", []),
        "scores": item.get("scores", {}),
        "is_open_source_project": item.get("is_open_source_project", False),
        "required_fields": {
            "what_is_it": "这是什么？",
            "problem": "解决了什么问题？",
            "method_or_contribution": "方法或贡献是什么？",
            "why_important": "为什么对我重要？",
            "deep_read": "是否建议深读？",
            "suggested_action": "建议行动，只能是 read_pdf / skim / watch / save / use_as_eval / clone_and_run / study_code / use_as_baseline / read_readme / archive / ignore 之一",
        },
    }
    messages = [
        {
            "role": "system",
            "content": (
                "你是严谨的 AI research radar 编辑，面向一位关注长上下文、Agent、开放世界学习和模型压缩的研究者。"
                "用自然、具体、克制的中文写摘要，不营销，不编造，不重复套话。"
                "grounding 不是禁止总结，而是禁止编造：允许基于 title、abstract、full text 或 README 做忠实中文归纳。"
                "禁止复制或截断英文 abstract；即使 grounding_level 是 abstract_only，也必须用中文概括。"
                "只基于 allowed_evidence 中真实出现的信息；信息不足时直接说明“方法细节未在摘要中充分展开”，最多在末尾补一句“细节需读原文确认”。"
                "如果写出具体数字、模型名、数据集名或 benchmark 结果，它必须能在 allowed_evidence 中逐字找到。"
                "grounding_level 为 title_only 或 abstract_only 时，不得扩展实验结论、系统细节或未给出的因果解释。"
                "避免模板化表达，不要按来源类型写泛泛的跟踪价值判断。"
                "不要反复使用空泛的免责句；只在确实缺信息时简短提示。"
                "返回严格 JSON，字段必须且只能包含："
                "what_is_it, problem, method_or_contribution, why_important, deep_read, suggested_action。"
                "suggested_action 只能是 read_pdf、skim、watch、save、use_as_eval、clone_and_run、study_code、use_as_baseline、read_readme、archive、ignore 之一。"
                "每个字段 1-2 句，尽量指出具体方法名、任务、数据、系统或实验线索。"
            ),
        },
        {"role": "user", "content": json.dumps(prompt, ensure_ascii=False)},
    ]
    try:
        from models.client import ChatModelClient, make_llm_cache_key

        client = ChatModelClient(
            provider=provider,
            api_key=api_key,
            base_url=base_url,
            model=model,
            timeout=openai_timeout_seconds(),
        )
        parsed = client.call_json(
            system_prompt=str(messages[0]["content"]),
            user_payload=str(messages[1]["content"]),
            temperature=0.2,
            max_tokens=max_output_tokens(),
            role="single_summary",
            cache_key=make_llm_cache_key(
                provider,
                model,
                "single_summary",
                str(item.get("title") or ""),
                str(item.get("url") or ""),
                str(item.get("abstract") or item.get("summary") or ""),
            ),
            required_fields=set(SUMMARY_FIELDS),
        )
        if parsed and all(key in parsed for key in SUMMARY_FIELDS):
            return normalize_summary(parsed, item)
        if parsed:
            record_llm_error(provider, model, base_url, "n/a", "Response JSON did not include all required summary fields.")
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as e:
        record_llm_error(provider, model, base_url, "n/a", str(e)[:500])
    except Exception as e:
        record_llm_error(provider, model, base_url, "n/a", str(e)[:500])
        return None
    return None


def llm_item_key(item: dict[str, Any]) -> str:
    return str(item.get("id") or item.get("url") or item.get("title") or id(item))


def llm_candidate_sort_key(item: dict[str, Any]) -> tuple[int, float, float, float, str]:
    tier = str(item.get("reading_tier") or "ARCHIVE").upper()
    tier_weight = {"MUST_READ": 3, "SKIM": 2, "WATCH": 1, "ARCHIVE": 0}.get(tier, 0)
    scores = item.get("scores", {}) if isinstance(item.get("scores"), dict) else {}
    return (
        tier_weight,
        float(scores.get("personal_score", 0.0) or 0.0),
        float(scores.get("research_relevance", 0.0) or 0.0),
        float(scores.get("global_score", 0.0) or 0.0),
        str(item.get("title") or ""),
    )


def llm_eligible_items(items: list[dict[str, Any]], tiers: set[str]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    candidates: list[dict[str, Any]] = []
    for item in items:
        key = llm_item_key(item)
        if key in seen:
            continue
        seen.add(key)
        tier = str(item.get("reading_tier") or "").upper()
        if tier not in tiers:
            continue
        if grounding_level(item) == "title_only":
            continue
        candidates.append(item)
    return sorted(candidates, key=llm_candidate_sort_key, reverse=True)


def prepare_llm_plan(items: list[dict[str, Any]]) -> None:
    global LLM_PLAN_READY
    global LLM_ITEMS_PROCESSED, ROLE_PIPELINE_ITEMS, SINGLE_LLM_ITEMS
    global ROLE_PIPELINE_ALLOWED_KEYS, SINGLE_LLM_ALLOWED_KEYS

    LLM_PLAN_READY = True
    LLM_ITEMS_PROCESSED = 0
    ROLE_PIPELINE_ITEMS = 0
    SINGLE_LLM_ITEMS = 0
    ROLE_PIPELINE_ALLOWED_KEYS = set()
    SINGLE_LLM_ALLOWED_KEYS = set()

    mode = configured_model_mode()
    if mode == "role_pipeline":
        role_limit = min(role_pipeline_budget(), max_llm_items())
        role_candidates = llm_eligible_items(items, {"MUST_READ"})[:role_limit]
        ROLE_PIPELINE_ALLOWED_KEYS = {llm_item_key(item) for item in role_candidates}

        single_limit = min(single_llm_budget(), max_llm_items())
        single_candidates = llm_eligible_items(items, {"SKIM"})[:single_limit]
        SINGLE_LLM_ALLOWED_KEYS = {llm_item_key(item) for item in single_candidates}
        return

    if mode == "single":
        single_limit = min(openai_summary_budget(), single_llm_budget(), max_llm_items())
        single_candidates = llm_eligible_items(items, {"MUST_READ", "SKIM"})[:single_limit]
        SINGLE_LLM_ALLOWED_KEYS = {llm_item_key(item) for item in single_candidates}


def summarize_item(item: dict[str, Any]) -> dict[str, Any]:
    global LLM_ITEMS_PROCESSED, ROLE_PIPELINE_ITEMS, SINGLE_LLM_ITEMS

    cached_summary = item.get("_cached_summary")
    if isinstance(cached_summary, dict):
        return normalize_summary(cached_summary, item)

    if not LLM_PLAN_READY:
        prepare_llm_plan([item])

    item_key = llm_item_key(item)
    mode = configured_model_mode()

    if mode == "role_pipeline" and item_key in ROLE_PIPELINE_ALLOWED_KEYS:
        ensemble_model = get_ensemble_model()
        if ensemble_model:
            try:
                result = ensemble_model.summarize(item)
                if result:
                    ROLE_PIPELINE_ITEMS += 1
                    LLM_ITEMS_PROCESSED += 1
                    return normalize_summary(result, item)
            except Exception as e:
                print(f"Ensemble model error: {e}")
        return fallback_summary(item)
    
    if item_key in SINGLE_LLM_ALLOWED_KEYS and has_any_llm_api_key():
        result = summarize_with_single_llm(item)
        if result:
            item["_cached_summary"] = {field: result.get(field, "") for field in SUMMARY_FIELDS}
            SINGLE_LLM_ITEMS += 1
            LLM_ITEMS_PROCESSED += 1
            return normalize_summary(result, item)
    
    return fallback_summary(item)


def score_line(item: dict[str, Any]) -> str:
    scores = item.get("scores", {})
    return (
        f"global_score {scores.get('global_score', 0):.2f}；"
        f"personal_score {scores.get('personal_score', 0):.2f}；"
        f"credibility {scores.get('credibility', 0):.2f}；"
        f"conference {scores.get('conference_signal', 0):.2f}；"
        f"institution {scores.get('institution_signal', 0):.2f}；"
        f"multi_source {scores.get('multi_source_confirmation', 0):.2f}；"
        f"community_signal {scores.get('community_signal', 0):.2f}；"
        f"actionability {scores.get('actionability', 0):.2f}；"
        f"research_relevance {scores.get('research_relevance', 0):.2f}；"
        f"hype_risk {scores.get('hype_risk', 0):.2f}"
    )


def source_role_label(item: dict[str, Any]) -> str:
    roles = item.get("source", {}).get("source_role")
    if not roles:
        return "未标注"
    if isinstance(roles, list):
        return "、".join(str(role) for role in roles)
    return str(roles)


def signal_line(item: dict[str, Any]) -> str:
    signals = item.get("source_signals", {})
    parts = []
    for label, key in [
        ("论文", "paper_sources"),
        ("顶会", "conference_sources"),
        ("机构", "institution_sources"),
        ("代码", "code_sources"),
        ("编辑", "editorial_sources"),
        ("产业", "industry_sources"),
        ("社区", "community_sources"),
        ("中文", "chinese_sources"),
    ]:
        values = signals.get(key) or []
        if values:
            parts.append(f"{label}:{'/'.join(values[:3])}")
    return "；".join(parts) or "无额外源信号"


def recommendation_explanation_line(item: dict[str, Any]) -> str:
    explanation = item.get("recommendation_explanation")
    if not isinstance(explanation, dict):
        return "尚未生成结构化解释"
    parts = []
    why = explanation.get("why_recommended") or []
    directions = explanation.get("matched_directions") or []
    top = explanation.get("top_features") or []
    if why:
        parts.append("；".join(str(value) for value in why[:2]))
    if directions:
        parts.append("命中方向：" + " / ".join(str(value) for value in directions[:3]))
    if top:
        parts.append("主要特征：" + ", ".join(f"{row.get('label')}={row.get('value')}" for row in top[:4] if isinstance(row, dict)))
    return "；".join(parts) or "规则排序命中，但贡献特征较分散"


def recommendation_risk_line(item: dict[str, Any]) -> str:
    explanation = item.get("recommendation_explanation")
    if not isinstance(explanation, dict):
        return "none"
    risks = explanation.get("risk_notes") or []
    return "；".join(str(value) for value in risks[:4]) or "none"


def recommendation_source_line(item: dict[str, Any]) -> str:
    explanation = item.get("recommendation_explanation")
    if not isinstance(explanation, dict):
        return str(item.get("source_layer") or "unknown")
    return (
        f"{explanation.get('source_class', 'unknown')}；"
        f"evidence={explanation.get('evidence_level', 'title_only')}；"
        f"primary={explanation.get('is_primary_source', False)}"
    )


def item_block(item: dict[str, Any], idx: int) -> str:
    source = item.get("source", {})
    kind = source.get("kind", "primary")
    published = item.get("published_at") or "未知"
    keywords = "、".join(item.get("matched_keywords", [])[:10]) or "无明显关键词"
    primary = item.get("primary_category") or item.get("primary_section", {})
    focus = section_display_name(primary.get("id", ""), primary.get("title", "未分类"))
    secondary_tags = "、".join(str(tag.get("title") or tag.get("id")) for tag in item.get("secondary_tags", [])[:8] if isinstance(tag, dict)) or "无"
    duplicate_names = sorted({s.get("name", "") for s in item.get("duplicate_sources", []) if s.get("name")})
    duplicate_text = "、".join(duplicate_names[:5]) if len(duplicate_names) > 1 else ""
    summary = summarize_item(item)
    tier_caption = "行动标签" if is_repository_item(item) else "阅读层级"

    lines = [
        f"##### {idx}. [{item.get('title')}]({item.get('url')})",
        f"- {tier_caption}：{TIER_LABELS.get(item.get('reading_tier'), item.get('reading_tier', 'ARCHIVE'))}",
        f"- 来源：{source.get('name', '未知')}",
        f"- 来源类型：{KIND_LABELS.get(kind, kind)}",
        f"- source_role：{source_role_label(item)}",
        f"- 证据来源：{grounding_label(item)}",
        f"- 原文链接：{item.get('url')}",
        f"- 发布时间：{published}",
        f"- 这是什么？{summary.get('what_is_it', '').strip()}",
        f"- 解决了什么问题？{summary.get('problem', '').strip()}",
        f"- 方法或贡献是什么？{summary.get('method_or_contribution', '').strip()}",
        f"- 为什么对我重要？{summary.get('why_important', '').strip()}",
        f"- 是否建议深读？{summary.get('deep_read', '').strip()}",
        f"- 建议行动：{summary.get('suggested_action', choose_action(item)).strip()}",
        f"- 评分：{score_line(item)}",
        f"- 多源信号：{signal_line(item)}",
        f"- 推荐解释：{recommendation_explanation_line(item)}",
        f"- 风险提示：{recommendation_risk_line(item)}",
        f"- 来源级别：{recommendation_source_line(item)}",
        f"- 命中方向：{focus}",
        f"- 相关标签：{secondary_tags}",
        f"- 命中关键词：{keywords}",
    ]
    if item.get("is_open_source_project"):
        metadata = item.get("metadata", {})
        metrics = item.get("metrics", {})
        if metrics.get("stars") is not None:
            stars = metrics.get("stars", 0)
            forks = metrics.get("forks", 0)
            license_info = metadata.get("license", "") or "未知"
            def signal_icon(value: Any) -> str:
                if value is True:
                    return "✅"
                if value is False:
                    return "❌"
                return "未知"

            has_examples = signal_icon(metadata.get("has_examples"))
            has_docs = signal_icon(metadata.get("has_docs"))
            has_repro = signal_icon(metadata.get("has_reproducible_script"))
            has_weights = signal_icon(metadata.get("has_pretrained_weights"))
            paper_link = metadata.get("paper_link", "")
            readme_summary = metadata.get("repo_readme_summary", "") or metadata.get("readme_excerpt", "")[:300]
            
            lines.append(f"- 开源信号：⭐ {stars} | 🍴 {forks} | 📜 {license_info}")
            lines.append(f"- 示例/文档/复现：示例 {has_examples} | 文档 {has_docs} | 脚本 {has_repro} | 权重 {has_weights}")
            if metadata.get("readme_fetch_status") and metadata.get("readme_fetch_status") != "ok":
                lines.append(f"- README 抓取状态：{metadata.get('readme_fetch_status')}，示例/文档/脚本字段按未知处理。")
            if paper_link:
                lines.append(f"- 关联论文：{paper_link}")
            if readme_summary:
                lines.append(f"- README 摘要：{readme_summary[:300]}")
        else:
            lines.append("- 开源信号：标题、摘要或来源中出现代码/开源线索。")
    if item.get("link_quality") == "low":
        lines.insert(5, "- link_quality: low")
    if duplicate_text:
        lines.append(f"- 去重信息：同一内容也出现在 {duplicate_text}")
    if item.get("requires_primary_source_check"):
        lines.append("- 风险提示：该条含发现/社区/中文媒体信号，结论需以论文、代码或官方公告为准。")
    return "\n".join(lines)


def compact_item(item: dict[str, Any]) -> str:
    section = item.get("primary_section", {}).get("title", "未分类")
    scores = item.get("scores", {})
    tier = item.get("reading_tier", "ARCHIVE")
    return (
        f"- [{item.get('title')}]({item.get('url')})"
        f"（{tier}，{section}，证据 {grounding_label(item)}，personal {scores.get('personal_score', 0):.2f}，global {scores.get('global_score', 0):.2f}）"
    )


def grouped_sections(
    processed: dict[str, Any],
    group: str | set[str],
    *,
    exclude_ids: set[str] | None = None,
) -> list[dict[str, Any]]:
    groups = {group} if isinstance(group, str) else group
    exclude_ids = exclude_ids or set()
    return [
        section
        for section in processed.get("sections", [])
        if section.get("group") in groups and section.get("id") not in exclude_ids
    ]


def score_rank(item: dict[str, Any]) -> tuple[float, float, float]:
    scores = item.get("scores", {})
    return (
        scores.get("personal_score", 0),
        scores.get("global_score", 0),
        scores.get("research_relevance", 0),
    )


def render_archive_titles(items: list[dict[str, Any]], limit: int = 8, label: str = "归档候选") -> list[str]:
    if not items:
        return []
    lines = ["", f"{label}："]
    for item in sorted(items, key=score_rank, reverse=True)[:limit]:
        lines.append(compact_item(item))
    return lines


def render_research_group(title: str, sections: list[dict[str, Any]]) -> list[str]:
    lines = [f"## {title}"]
    single_same_title = len(sections) == 1 and sections[0].get("title") == title
    for section in sections:
        group = section.get("group")
        section_id = section.get("id")
        items = sorted(
            [item for item in section.get("items", []) if item.get("reading_tier") != "IGNORE"],
            key=score_rank,
            reverse=True,
        )
        must_items = [item for item in items if item.get("reading_tier") == "MUST_READ"]
        skim_items = [item for item in items if item.get("reading_tier") == "SKIM"]
        watch_items = [item for item in items if item.get("reading_tier") == "WATCH"]
        archive_items = [item for item in items if item.get("reading_tier") == "ARCHIVE"]

        lines.append("")
        if not single_same_title:
            lines.append(f"### {section.get('title')}")

        if group in {"core_focus", "primary_research"}:
            body_items = must_items[:1] + skim_items[:2]
            if body_items:
                for idx, item in enumerate(body_items, 1):
                    lines.append(item_block(item, idx))
                    lines.append("")
            else:
                lines.append("- 今日没有 MUST_READ / SKIM 条目。")
            lines.extend(render_archive_titles(watch_items, limit=6, label="WATCH 跟踪"))
            lines.extend(render_archive_titles(archive_items))
            continue

        if group in {"traditional_ai", "traditional_fields"}:
            shown_items = (must_items + skim_items + watch_items + archive_items)[:2]
        elif group == "other" or section_id == "highlights":
            shown_items = (must_items + skim_items + watch_items + archive_items)[:5]
        else:
            shown_items = must_items + skim_items + watch_items + archive_items

        if shown_items:
            for idx, item in enumerate(shown_items, 1):
                lines.append(item_block(item, idx))
                lines.append("")
        else:
            lines.append("- 今日没有 MUST_READ / SKIM 条目。")
    lines.append("")
    return lines


def unique_section_items(sections: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_key: dict[str, dict[str, Any]] = {}
    for section in sections:
        for item in section.get("items", []):
            if item.get("reading_tier") == "IGNORE":
                continue
            key = item.get("id") or item.get("url") or item.get("title")
            existing = by_key.get(key)
            if not existing or score_rank(item) > score_rank(existing):
                by_key[key] = item
    return sorted(by_key.values(), key=score_rank, reverse=True)


def render_other_highlights(sections: list[dict[str, Any]]) -> list[str]:
    lines = ["## Other Highlights"]
    items = unique_section_items(sections)[:5]
    if not items:
        lines.append("- 今日没有进入正文的 Other Highlights。")
        lines.append("")
        return lines
    for idx, item in enumerate(items, 1):
        lines.append(item_block(item, idx))
        lines.append("")
    return lines


def _classify_github_project(item: dict[str, Any]) -> str:
    metadata = item.get("metadata", {})
    bucket = metadata.get("github_bucket")
    if bucket in {"recent", "paper_linked", "evergreen"}:
        return str(bucket)
    is_paper_linked = item.get("is_paper_linked", False) or item.get("paper_reference")
    if metadata.get("paper_link"):
        is_paper_linked = True
    created_at = metadata.get("created_at")
    updated_at = metadata.get("updated_at")
    
    is_recently_active = False
    if updated_at:
        try:
            from datetime import datetime
            updated_date = datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
            days_since_update = (datetime.now() - updated_date).days
            is_recently_active = days_since_update <= 7
        except:
            pass
    
    is_new = False
    if created_at:
        try:
            from datetime import datetime
            created_date = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
            days_since_creation = (datetime.now() - created_date).days
            is_new = days_since_creation <= 30
        except:
            pass
    
    if is_new or is_recently_active:
        return "recent"
    if is_paper_linked:
        return "paper_linked"
    return "evergreen"


def _is_project_recently_recommended(item: dict[str, Any], days_threshold: int = 30) -> bool:
    last_recommended = item.get("last_recommended")
    if not last_recommended:
        return False
    
    try:
        from datetime import datetime
        recommended_date = datetime.fromisoformat(last_recommended.replace("Z", "+00:00"))
        days_since_recommended = (datetime.now() - recommended_date).days
        return days_since_recommended < days_threshold
    except:
        return False


def render_github_projects(projects: list[dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    
    recent_projects = []
    paper_linked_projects = []
    evergreen_projects = []
    
    for item in projects:
        if _is_project_recently_recommended(item):
            metrics = item.get("metrics", {})
            stars = metrics.get("stars", 0) or 0
            prev_stars = metrics.get("prev_stars", 0) or 0
            star_growth = stars - prev_stars
            
            if star_growth > 100 or item.get("is_major_release") or item.get("new_paper_citation"):
                pass
            else:
                continue
        
        category = _classify_github_project(item)
        if category == "recent":
            recent_projects.append(item)
        elif category == "paper_linked":
            paper_linked_projects.append(item)
        else:
            evergreen_projects.append(item)
    
    if not recent_projects and not paper_linked_projects and not evergreen_projects:
        lines.append("- 今日没有进入正文的开源项目候选。")
        lines.append("")
        return lines
    
    lines.append("### New / Recently Active Projects")
    if recent_projects:
        for idx, item in enumerate(recent_projects[:3], 1):
            lines.append(item_block(item, idx))
            lines.append("")
    else:
        lines.append("- 今日无新增或近期活跃项目。")
        lines.append("")

    lines.append("### Paper-linked Repos")
    if paper_linked_projects:
        for idx, item in enumerate(paper_linked_projects[:3], 1):
            lines.append(item_block(item, idx))
            lines.append("")
    else:
        lines.append("- 今日无可靠论文链接仓库。")
        lines.append("")

    lines.append("### Evergreen Toolkits")
    if evergreen_projects:
        for idx, item in enumerate(evergreen_projects[:3], 1):
            lines.append(item_block(item, idx))
            lines.append("")
    else:
        lines.append("- 今日无需要重复推荐的常青工具库。")
        lines.append("")
    
    return lines


def render_classics(classics: list[dict[str, Any]]) -> list[str]:
    lines = ["## 温故而知新 / Classic Paper Revisit"]
    if not classics:
        lines.append("- 今日没有足够明确的主题连接，暂不推荐经典论文。")
        lines.append("")
        return lines

    for idx, paper in enumerate(classics, 1):
        related_sections = "、".join(paper.get("related_sections", [])) or "相关方向"
        authors = "、".join(str(author) for author in paper.get("authors", [])[:8])
        if len(paper.get("authors", [])) > 8:
            authors += " 等"
        topic_tags = "、".join(str(tag) for tag in paper.get("topic_tags", [])[:8])
        lines.extend(
            [
                f"### {idx}. [{paper.get('title')}]({paper.get('url')})（{paper.get('year')}）",
                f"- 作者：{authors or '未知'}",
                f"- topic_tags：{topic_tags or '未标注'}",
                f"- 关联方向：{related_sections}",
                f"- 为什么经典：{paper.get('why_classic') or paper.get('why_now')}",
            ]
        )
        concept = paper.get("concept_connection") or {}
        if concept:
            lines.append(f"- 今日新论文继承了什么问题：{concept.get('inherits', '需要打开今日论文确认。')}")
            lines.append(f"- 它挑战了什么经典假设：{concept.get('challenges', '需要打开今日论文确认。')}")
            lines.append(f"- 它推进到什么新场景：{concept.get('extends', '需要打开今日论文确认。')}")
        else:
            lines.append(f"- 它和今日新论文的概念连接：{paper.get('modern_connection', '今天没有足够明确的新论文连接；作为基础脉络复习。')}")
        if paper.get("prerequisite"):
            lines.append(f"- 预备知识：{paper.get('prerequisite')}")
        related_today = paper.get("related_today", [])
        if related_today:
            lines.append("- 相关今日条目：")
            for item in related_today:
                terms = "、".join(item.get("connection_terms", []))
                suffix = f"；连接词：{terms}" if terms else ""
                lines.append(f"  - [{item.get('title')}]({item.get('url')})（{item.get('section')}{suffix}）")
        lines.append("")
    return lines


def section_display_name(section_id: str, fallback: str | None = None) -> str:
    return SECTION_DISPLAY_NAMES.get(section_id, fallback or section_id)


def get_section(processed: dict[str, Any], section_id: str) -> dict[str, Any]:
    for section in processed.get("sections", []):
        if section.get("id") == section_id:
            return section
    return {"id": section_id, "title": section_display_name(section_id), "items": []}


def items_for_section(processed: dict[str, Any], section_ids: list[str]) -> list[dict[str, Any]]:
    by_key: dict[str, dict[str, Any]] = {}
    for section_id in section_ids:
        for item in get_section(processed, section_id).get("items", []):
            if item.get("reading_tier") == "IGNORE":
                continue
            key = item.get("id") or item.get("url") or item.get("title")
            existing = by_key.get(key)
            if not existing or score_rank(item) > score_rank(existing):
                by_key[key] = item
    return sorted(by_key.values(), key=score_rank, reverse=True)


def items_by_tier(items: list[dict[str, Any]], tier: str) -> list[dict[str, Any]]:
    return [item for item in items if item.get("reading_tier") == tier]


def render_full_items(items: list[dict[str, Any]], *, limit: int = 3, empty: str = "- 无。") -> str:
    if not items:
        return empty
    blocks = [item_block(item, idx) for idx, item in enumerate(items[:limit], 1)]
    return "\n\n".join(blocks)


def render_compact_items(items: list[dict[str, Any]], *, limit: int = 6, empty: str = "- 无。") -> str:
    if not items:
        return empty
    return "\n".join(compact_item(item) for item in items[:limit])


def render_primary_section(processed: dict[str, Any], section_ids: list[str]) -> dict[str, str]:
    items = items_for_section(processed, section_ids)
    return {
        "must_read": render_full_items(items_by_tier(items, "MUST_READ"), limit=1),
        "skim": render_full_items(items_by_tier(items, "SKIM"), limit=2),
        "watch": render_compact_items(items_by_tier(items, "WATCH"), limit=3),
        "archive": render_compact_items(items_by_tier(items, "ARCHIVE"), limit=8),
    }


def render_traditional_section(processed: dict[str, Any], section_id: str) -> str:
    items = items_for_section(processed, [section_id])
    shown = items_by_tier(items, "MUST_READ") + items_by_tier(items, "SKIM") + items_by_tier(items, "WATCH") + items_by_tier(items, "ARCHIVE")
    return render_compact_items(shown, limit=2, empty="- 今日无明显条目。")


def has_official_or_multi_source_signal(item: dict[str, Any]) -> bool:
    source = item.get("source", {})
    text = " ".join(
        [
            str(source.get("id", "")),
            str(source.get("name", "")),
            str(source.get("url", "")),
            str(item.get("url", "")),
        ]
    ).lower()
    official = any(
        token in text
        for token in [
            "openai",
            "anthropic",
            "deepmind",
            "google",
            "meta",
            "microsoft",
            "nvidia",
            "apple",
            "stanford",
            "mit",
            "berkeley",
            "neurips",
            "icml",
            "iclr",
            "thecvf",
        ]
    )
    return official or len(item.get("duplicate_sources", []) or []) > 1 or item.get("is_open_source_project")


def is_strict_other_highlight(item: dict[str, Any]) -> bool:
    scores = item.get("scores", {})
    source_type = str(item.get("source", {}).get("type", "")).lower()
    plain_arxiv = source_type in {"arxiv", "hf_daily_papers", "hf_papers_page"}
    strong_signal = (
        has_official_or_multi_source_signal(item)
        or scores.get("community_signal", 0) >= 0.25
        or scores.get("actionability", 0) >= 0.72
    )
    if plain_arxiv and not strong_signal:
        return False
    return (
        scores.get("global_score", 0) >= 0.78
        and scores.get("credibility", 0) >= 0.75
        and scores.get("evidence_strength", 0) >= 0.65
        and strong_signal
    )


def _classify_institutional_update(item: dict[str, Any]) -> str:
    title = item.get("title", "").lower()
    summary = item.get("summary", "").lower()
    text = title + " " + summary
    
    if any(term in text for term in ["research", "paper", "preprint", "arxiv", "publication", "study", "findings"]):
        return "Research Release"
    if any(term in text for term in ["product", "api", "service", "feature", "launch", "release", "update"]):
        return "Product / API Release"
    if any(term in text for term in ["partnership", "collaboration", "alliance", "policy", "regulation", "announcement"]):
        return "Partnership / Policy"
    if any(term in text for term in ["case study", "use case", "application", "deployment", "customer"]):
        return "Application Case"
    if "pull request" in text or "pr" in text or "github pr" in text:
        return "Low-signal PR"
    return "Research Release"


def item_title_link(item: dict[str, Any]) -> str:
    title = item.get("title") or "Untitled"
    url = item.get("url")
    return f"[{title}]({url})" if url else title


def institutional_research_value(item: dict[str, Any]) -> str:
    scores = item.get("scores", {})
    personal = scores.get("personal_score", 0.0)
    relevance = scores.get("research_relevance", 0.0)
    if max(personal, relevance) >= 0.75:
        return "高"
    if max(personal, relevance) >= 0.55:
        return "中"
    return "低"


def institutional_advice(item: dict[str, Any]) -> str:
    scores = item.get("scores", {})
    tier = item.get("reading_tier")
    if scores.get("personal_score", 0.0) < 0.45 or tier == "ARCHIVE":
        return "archive"
    if tier == "SKIM":
        return "skim"
    if tier in {"MUST_READ", "WATCH"}:
        return "follow"
    return "archive"


def institutional_substance(item: dict[str, Any]) -> str:
    summary = trim(item.get("summary", ""), 220)
    return summary or item.get("title", "")


def institutional_item_block(item: dict[str, Any], category: str) -> str:
    scores = item.get("scores", {})
    tier = item.get("reading_tier")
    if category == "Low-signal PR" or (tier == "ARCHIVE" and scores.get("personal_score", 0.0) < 0.45):
        return f"- {item_title_link(item)}"
    return "\n".join(
        [
            f"- {item_title_link(item)}",
            f"  - 类型：{category}",
            f"  - 实质：{institutional_substance(item)}",
            f"  - 研究价值：{institutional_research_value(item)}；建议：{institutional_advice(item)}",
        ]
    )


def render_institutional_updates(processed: dict[str, Any]) -> str:
    items = items_for_section(processed, ["institutional_updates"])
    if not items:
        return "- 今日无机构动态。"
    
    categorized = {
        "Research Release": [],
        "Product / API Release": [],
        "Partnership / Policy": [],
        "Application Case": [],
        "Low-signal PR": [],
    }
    
    for item in items:
        category = _classify_institutional_update(item)
        categorized[category].append(item)
    
    lines = []
    for category in ["Research Release", "Product / API Release", "Partnership / Policy", "Application Case", "Low-signal PR"]:
        if categorized[category]:
            lines.append(f"### {category}")
            for item in categorized[category][:3]:
                lines.append(institutional_item_block(item, category))
                lines.append("")
            if len(categorized[category]) > 3:
                lines.append(f"- ... 还有 {len(categorized[category]) - 3} 条")
            lines.append("")
    
    return "\n".join(lines).strip()


def render_other_section(processed: dict[str, Any], section_ids: list[str], *, limit: int = 5) -> str:
    if "institutional_updates" in section_ids:
        return render_institutional_updates(processed)
    
    items = items_for_section(processed, section_ids)
    if any(section_id in {"highlights", "other_highlights"} for section_id in section_ids):
        strict = [
            item
            for item in items
            if item.get("reading_tier") in {"MUST_READ", "SKIM", "WATCH"} and is_strict_other_highlight(item)
        ]
        other_watch = [
            item
            for item in items
            if item not in strict and item.get("reading_tier") in {"WATCH", "ARCHIVE"}
        ]
        lines = [render_full_items(strict, limit=limit, empty="- 今日没有达到高影响阈值的 Other Highlights。")]
        if other_watch:
            lines.append("")
            lines.append("Other Watch / Archive：")
            lines.append(render_compact_items(other_watch, limit=8))
        return "\n".join(lines)
    shown = items_by_tier(items, "MUST_READ") + items_by_tier(items, "SKIM") + items_by_tier(items, "WATCH") + items_by_tier(items, "ARCHIVE")
    return render_full_items(shown, limit=limit, empty="- 今日无明显条目。")


def benchmark_ability(item: dict[str, Any]) -> str:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    if "workflow fidelity" in text or "payment" in text:
        return "评估 LLM agent 在真实/拟真 workflow 中是否按预期完成轨迹与关键步骤。"
    if "video action" in text or "viddiff" in text:
        return "评估多模态模型区分同一动作视频之间细粒度语义差异的能力。"
    if "spatialepi" in text or "epidemic" in text:
        return "评估时空流行病预测中空间信息、流行病先验和滚动预测协议的有效性。"
    if "medarabench" in text or "arabic medical" in text:
        return "评估阿拉伯语医学多项选择问答与多语言医学能力。"
    if "agent" in text or "planning" in text:
        return "评估 agent 规划、执行或环境交互能力。"
    if "dataset" in text or "benchmark" in text or "evaluation" in text:
        return "评估摘要中描述的任务能力；具体指标需打开原文确认。"
    return "标题信号不足，需打开原文确认评估对象。"


def benchmark_fit(item: dict[str, Any]) -> str:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    if "workflow fidelity" in text or "payment" in text:
        return "适合用于 agent evaluation、long-horizon workflow、轨迹保真度和安全执行研究。"
    if "video action" in text or "viddiff" in text:
        return "适合用于 VLM/视频理解中的细粒度动作差异评测，不是当前四条主线的核心实验。"
    if "spatialepi" in text or "epidemic" in text:
        return "适合用于 AI for science、时空预测和科学 benchmark 设计参考。"
    if "medarabench" in text or "arabic medical" in text:
        return "适合用于多语言医学 QA、低资源语言评测和领域安全性测试。"
    if any(term in text for term in ["agent", "planning", "memory", "long context", "safety"]):
        return "适合用于 agent evaluation / memory / long-horizon planning 相关实验。"
    if any(term in text for term in ["domain generalization", "multimodal"]):
        return "适合用于多模态泛化或跨域评测设计参考。"
    return "适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。"


def benchmark_baseline_use(item: dict[str, Any]) -> str:
    action = benchmark_action(item)
    if action == "use_as_eval":
        return "可以优先评估是否作为实验基准。"
    if action in {"skim", "save"}:
        return "暂不作为核心基准，先保存评测协议和指标设计。"
    return "不建议作为当前实验基准。"


def benchmark_layer(item: dict[str, Any]) -> str:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    scores = item.get("scores", {})
    core_terms = [
        "agent",
        "workflow",
        "planning",
        "long-horizon",
        "long horizon",
        "memory",
        "safety",
        "ood",
        "open-world",
        "distillation",
        "compression",
    ]
    if any(term in text for term in core_terms) and (
        scores.get("personal_score", 0) >= 0.62 or scores.get("research_relevance", 0) >= 0.65
    ):
        return "core"
    if scores.get("global_score", 0) >= 0.62 or scores.get("actionability", 0) >= 0.55:
        return "interesting"
    return "other"


def benchmark_block(item: dict[str, Any], idx: int) -> str:
    source = item.get("source", {})
    tier = item.get("reading_tier", "ARCHIVE")
    action = benchmark_action(item)
    return "\n".join(
        [
            f"##### {idx}. [{item.get('title')}]({item.get('url')})",
            f"- 阅读层级：{tier}",
            f"- 来源：{source.get('name', '未知')}",
            f"- 证据来源：{grounding_label(item)}",
            f"- benchmark 评估什么能力：{benchmark_ability(item)}",
            f"- 适合用于什么研究：{benchmark_fit(item)}",
            f"- 可否作为实验基准：{benchmark_baseline_use(item)}",
            f"- 建议行动：{action}",
        ]
    )


def benchmark_items(processed: dict[str, Any]) -> list[dict[str, Any]]:
    items = items_for_section(processed, ["benchmark_evaluation"])
    shown = items_by_tier(items, "MUST_READ") + items_by_tier(items, "SKIM") + items_by_tier(items, "WATCH") + items_by_tier(items, "ARCHIVE")
    return shown


def benchmark_appendix_path(report_date: str) -> Path:
    return Path("reports") / "appendix" / f"{report_date}-benchmarks.md"


def write_benchmark_appendix(processed: dict[str, Any], report_date: str) -> str:
    other = [item for item in benchmark_items(processed) if benchmark_layer(item) == "other"]
    if not other:
        return ""
    path = benchmark_appendix_path(report_date)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Other Benchmarks - {report_date}",
        "",
        "以下条目只列标题，未在日报正文展开。",
        "",
    ]
    for item in other:
        lines.append(compact_item(item))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(path).replace("\\", "/")


def render_benchmark_section(processed: dict[str, Any], *, report_date: str, limit: int | None = None) -> str:
    shown = benchmark_items(processed)
    if not shown:
        return "- 今日无明显 benchmark / dataset / evaluation 条目。"
    core = [item for item in shown if benchmark_layer(item) == "core"][:5]
    interesting = [item for item in shown if benchmark_layer(item) == "interesting"][:5]
    other = [item for item in shown if benchmark_layer(item) == "other"]
    if limit is not None:
        core = core[:limit]
        interesting = interesting[: max(0, limit - len(core))]
    lines: list[str] = ["### Core Benchmarks for My Research"]
    lines.append(
        "\n\n".join(benchmark_block(item, idx) for idx, item in enumerate(core, 1))
        if core
        else "- 今日没有核心 benchmark。"
    )
    lines.extend(["", "### Interesting Benchmarks"])
    lines.append(
        "\n\n".join(benchmark_block(item, idx) for idx, item in enumerate(interesting, 1))
        if interesting
        else "- 今日没有额外值得展开的 benchmark。"
    )
    lines.extend(["", "### Other Benchmarks"])
    appendix = benchmark_appendix_path(report_date)
    if other:
        lines.append(f"- 其余 {len(other)} 个只进入附录标题列表：{str(appendix).replace(chr(92), '/')}")
    else:
        lines.append("- 无。")
    return "\n".join(lines)


def all_non_ignored_items(processed: dict[str, Any]) -> list[dict[str, Any]]:
    return [item for item in processed.get("items", []) if item.get("reading_tier") != "IGNORE"]


def recommendation_action(item: dict[str, Any]) -> str:
    if item.get("reading_tier") == "MUST_READ":
        return "read_pdf"
    if item.get("reading_tier") == "SKIM":
        return "skim"
    if item.get("is_open_source_project"):
        return item.get("github_action") or "read_readme"
    if item.get("requires_primary_source_check"):
        return "verify_primary_source"
    return "watch"


def render_awards_notable_papers(processed: dict[str, Any], *, limit: int = 5) -> str:
    candidates = []
    for item in all_non_ignored_items(processed):
        conference = item.get("conference", {})
        if conference.get("conference_signal_status") != "confirmed":
            continue
        signal = item.get("scores", {}).get("conference_signal", 0.0)
        award = conference.get("award_type")
        presentation = conference.get("presentation_type")
        relevant_accepted = award == "accepted" and item.get("scores", {}).get("research_relevance", 0.0) >= 0.70
        if not conference.get("conference_name") or (signal < 0.50 and not relevant_accepted):
            continue
        if award == "accepted" and not relevant_accepted:
            continue
        candidates.append(item)
    candidates.sort(
        key=lambda item: (
            item.get("scores", {}).get("conference_signal", 0.0),
            item.get("scores", {}).get("personal_score", 0.0),
            item.get("scores", {}).get("research_relevance", 0.0),
        ),
        reverse=True,
    )
    if not candidates:
        return "- 今日无高相关顶会精选。"
    lines = []
    for item in candidates[:limit]:
        conference = item.get("conference", {})
        authority = item.get("authority", {})
        institutions = "、".join(row.get("name") for row in authority.get("matched_institutions", []) if row.get("name")) or "待从原文确认"
        signal_type = conference.get("award_type") or conference.get("presentation_type") or "conference_signal"
        year = conference.get("conference_year") or "年份待确认"
        evidence_source = conference.get("evidence_source") or "metadata"
        lines.extend(
            [
                f"- 会议 / 年份 / 信号类型：{conference.get('conference_name')} / {year} / {signal_type}",
                f"  - 论文标题：[{item.get('title')}]({item.get('url')})",
                f"  - evidence_source：{evidence_source}",
                f"  - 作者机构：{institutions}",
                f"  - 方向标签：{section_title_from_item(item)}",
                f"  - 和我的研究方向关系：research_relevance {item.get('scores', {}).get('research_relevance', 0):.2f}",
                f"  - 建议行动：{recommendation_action(item)}",
            ]
        )
    return "\n".join(lines)


def lab_item_type(item: dict[str, Any]) -> str:
    source_type = str(item.get("source", {}).get("type", "")).lower()
    text = f"{item.get('title', '')} {item.get('summary', '')} {item.get('url', '')}".lower()
    if source_type in {"arxiv", "openreview", "hf_daily_papers", "hf_papers_page"}:
        return "paper"
    if item.get("is_open_source_project") or "github.com" in text:
        return "project"
    if any(term in text for term in ["course", "syllabus", "lecture", "reading list"]):
        return "course"
    if any(term in text for term in ["seminar", "talk", "workshop"]):
        return "seminar"
    if any(term in text for term in ["dataset", "benchmark"]):
        return "dataset"
    return "blog"


def recent_daily_report_text(report_date: str, *, days: int = 30) -> str:
    try:
        current = datetime.strptime(report_date, "%Y-%m-%d")
    except ValueError:
        return ""
    pieces = []
    for offset in range(1, days + 1):
        day = current - timedelta(days=offset)
        path = Path("reports") / "daily" / day.strftime("%Y") / day.strftime("%m") / f"{day.strftime('%Y-%m-%d')}.md"
        if path.exists():
            pieces.append(path.read_text(encoding="utf-8", errors="ignore"))
    return normalize_report_text("\n".join(pieces))


def normalize_report_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).lower()


def repeated_evergreen_lab_item(item: dict[str, Any], recent_text: str) -> bool:
    if not recent_text:
        return False
    title = normalize_report_text(str(item.get("title", "")))
    if not title or len(title) < 12:
        return False
    if lab_item_type(item) in {"course", "seminar"} or any(term in title for term in ["course", "reading list", "seminar", "lecture"]):
        return title in recent_text
    return False


def render_university_lab_radar(processed: dict[str, Any], *, report_date: str, limit: int = 5) -> str:
    recent_text = recent_daily_report_text(report_date)
    candidates = []
    for item in all_non_ignored_items(processed):
        authority = item.get("authority", {})
        matched = authority.get("matched_institutions", [])
        if not matched:
            continue
        source_roles = item.get("source", {}).get("source_role") or []
        if isinstance(source_roles, str):
            source_roles = [source_roles]
        if "institution_authority" not in source_roles and item.get("scores", {}).get("institution_signal", 0.0) < 0.72:
            continue
        title = str(item.get("title", "")).lower()
        if title in {"home", "homepage", "research", "people", "publications"}:
            continue
        if repeated_evergreen_lab_item(item, recent_text):
            continue
        candidates.append(item)
    candidates.sort(
        key=lambda item: (
            item.get("scores", {}).get("institution_signal", 0.0),
            item.get("scores", {}).get("personal_score", 0.0),
            item.get("scores", {}).get("actionability", 0.0),
        ),
        reverse=True,
    )
    if not candidates:
        return "- 今日无高相关强校/实验室雷达条目。"
    lines = []
    for item in candidates[:limit]:
        authority = item.get("authority", {})
        matched = authority.get("matched_institutions", [])
        lab = matched[0].get("name") if matched else authority.get("lab_or_group") or item.get("source", {}).get("name", "未知机构")
        item_type = lab_item_type(item)
        scores = item.get("scores", {})
        lines.extend(
            [
                f"- [{item.get('title')}]({item.get('url')})",
                f"  - 学校 / 实验室：{lab}",
                f"  - 类型：{item_type}",
                f"  - 为什么值得关注：institution_signal {scores.get('institution_signal', 0):.2f}，authority_score {scores.get('authority_score', 0):.2f}",
                f"  - 与我的研究方向关系：{section_title_from_item(item)}，personal {scores.get('personal_score', 0):.2f}",
                f"  - 建议行动：{recommendation_action(item)}",
            ]
        )
    return "\n".join(lines)


def render_context_community_signals(processed: dict[str, Any], *, limit: int = 5) -> str:
    candidates = []
    for item in all_non_ignored_items(processed):
        signals = item.get("source_signals", {})
        has_context_signal = any(
            signals.get(key)
            for key in ["chinese_sources", "community_sources", "discovery_sources"]
        )
        if has_context_signal or item.get("requires_primary_source_check"):
            candidates.append(item)
    candidates.sort(
        key=lambda item: (
            item.get("scores", {}).get("community_signal", 0.0),
            item.get("scores", {}).get("hype_risk", 0.0),
            item.get("scores", {}).get("personal_score", 0.0),
        ),
        reverse=True,
    )
    if not candidates:
        return "- 今日无需要展开的中文媒体或社区线索。"
    lines = []
    for item in candidates[:limit]:
        signals = item.get("source_signals", {})
        source_type = "社区/发现线索"
        if signals.get("chinese_sources"):
            source_type = "中文媒体线索"
        scores = item.get("scores", {})
        primary_status = "已匹配一手来源" if scores.get("credibility", 0) >= 0.75 or signals.get("paper_sources") else "待查"
        lines.extend(
            [
                f"- [{item.get('title')}]({item.get('url')})",
                f"  - 类型：{source_type}",
                f"  - 一手来源：{primary_status}",
                f"  - hype_risk：{scores.get('hype_risk', 0):.2f}",
                f"  - 建议行动：verify_primary_source",
            ]
        )
    return "\n".join(lines)


def source_count(processed: dict[str, Any]) -> int:
    source_ids = {
        item.get("source", {}).get("id")
        for item in processed.get("items", [])
        if item.get("source", {}).get("id")
    }
    for item in processed.get("items", []):
        for source in item.get("duplicate_sources", []) or []:
            if source.get("id"):
                source_ids.add(source["id"])
    return len(source_ids)


def render_source_health(processed: dict[str, Any]) -> str:
    events = processed.get("source_health") or []
    if not events:
        return "- No source health warnings recorded."
    lines: list[str] = []
    for event in events:
        if not isinstance(event, dict):
            continue
        source = event.get("source") or "unknown source"
        status = event.get("status") or "warning"
        detail = event.get("detail") or ""
        items = event.get("items")
        suffix = f" ({items} items)" if items not in (None, "") else ""
        lines.append(f"- {source}: {status}{suffix}" + (f" - {detail}" if detail else ""))
    return "\n".join(lines) if lines else "- No source health warnings recorded."


def top_keywords(items: list[dict[str, Any]], *, limit: int = 10) -> str:
    counter: Counter[str] = Counter()
    for item in items:
        for keyword in item.get("matched_keywords", [])[:10]:
            text = str(keyword).strip()
            if text and len(text) <= 40:
                counter[text] += 1
    return "、".join(keyword for keyword, _ in counter.most_common(limit)) or "无明显集中关键词"


def section_title_from_item(item: dict[str, Any]) -> str:
    section = item.get("primary_section", {})
    return section_display_name(section.get("id", ""), section.get("title", "未分类"))


def _extract_trend_keywords(items: list[dict[str, Any]]) -> list[str]:
    keywords = []
    for item in items:
        title = item.get("title", "").lower()
        summary = item.get("summary", "").lower()
        matched_kw = [str(k).lower() for k in item.get("matched_keywords", [])]
        combined = title + " " + summary + " " + " ".join(matched_kw)
        if "agent" in combined and ("memory" in combined or "retrieval" in combined or "knowledge" in combined):
            keywords.append("Agent记忆/检索")
        if "vlm" in combined or "vision" in combined or "distill" in combined:
            keywords.append("VLM蒸馏")
        if "ranking" in combined or "clip" in combined or "dinov" in combined or "dino" in combined:
            keywords.append("多模态排序")
        if "reasoning" in combined and ("llm" in combined or "model" in combined):
            keywords.append("LLM推理")
        if "fine-tun" in combined or "lora" in combined or "parameter-eff" in combined:
            keywords.append("参数高效微调")
        if "long-context" in combined or "context-window" in combined:
            keywords.append("长上下文")
        if "reward" in combined and ("model" in combined or "rl" in combined):
            keywords.append("奖励模型/RL")
        if "world-model" in combined or "plann" in combined:
            keywords.append("世界模型/规划")
        if "multi-agent" in combined or ("multi" in combined and "agent" in combined):
            keywords.append("多智能体")
    return keywords


def _analyze_must_read_trends(must: list[dict[str, Any]]) -> dict[str, list[str]]:
    trends = {}
    for item in must:
        title = item.get("title", "").lower()
        summary = item.get("summary", "").lower()
        combined = title + " " + summary
        
        section_id = item.get("primary_section", {}).get("id", "")
        section_title = item.get("primary_section", {}).get("title", "")
        
        if "stale" in title or "memory valid" in combined or "memory staleness" in combined:
            trends.setdefault("memory_validity", []).append(item)
        elif "agent" in combined and ("memory" in combined or "belief" in combined):
            trends.setdefault("agent_memory", []).append(item)
        elif "agent" in combined and ("trajectory" in combined or "workflow" in combined or "long-horizon" in combined):
            trends.setdefault("agent_trajectory", []).append(item)
        elif section_id in {"context_compression_memory", "context_compression", "context_memory"}:
            trends.setdefault("context_compression", []).append(item)
        elif section_id == "agents":
            trends.setdefault("agents", []).append(item)
        elif section_id in {"model_distillation", "distillation_efficiency"}:
            if "dinorankclip" in title or "ranking" in combined or "clip" in title:
                trends.setdefault("distillation_ranking", []).append(item)
            else:
                trends.setdefault("distillation", []).append(item)
        elif "vlm" in combined or "vision-language" in combined:
            trends.setdefault("vlm", []).append(item)
        elif "benchmark" in combined or "evaluation" in combined:
            trends.setdefault("benchmark", []).append(item)
        else:
            trends.setdefault("other", []).append(item)
    
    return trends


def _generate_trend_judgement(must: list[dict[str, Any]], direction: str) -> str:
    if not must:
        return "今日主线：没有强制深读项，建议归档观察。"

    combined = "\n".join(
        f"{item.get('title', '')} {item.get('summary', '')} {item.get('primary_section', {}).get('id', '')}"
        for item in must
    ).lower()
    judgements: list[str] = []

    if "adaptive parallel reasoning" in combined or ("parallel" in combined and "reasoning" in combined):
        judgements.append("推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径")
    if "stale" in combined or "memory validity" in combined or "memory staleness" in combined:
        judgements.append("Agent memory 的重点从“存更多”转向判断记忆何时失效、何时需要被新证据覆盖")
    if "agentic rl" in combined or ("reinforcement learning" in combined and "agent" in combined):
        judgements.append("Agentic RL 正从单次结果打分推进到长程轨迹、环境反馈和策略更新的闭环")
    if "novel class" in combined or "open-world" in combined or "open world" in combined:
        judgements.append("开放世界学习继续从封闭类别识别转向新类发现、未知类处理和持续更新")
    if "continuous-time distribution" in combined or ("diffusion" in combined and "distillation" in combined):
        judgements.append("模型蒸馏在 diffusion 方向从离散步监督走向连续时间分布匹配")
    elif "distillation" in combined or "compression" in combined:
        judgements.append("模型压缩的关注点从单纯变小转向保留推理结构、排序一致性和部署可用性")
    if "context compression" in combined or "kv cache" in combined or "long context" in combined:
        judgements.append("长上下文方向正在把上下文压缩、KV cache 复用和 agent 状态管理合并考虑")

    if judgements:
        if len(judgements) == 1:
            return f"今日主线：{judgements[0]}。"
        return f"今日主线：{judgements[0]}；同时 {judgements[1]}。"

    title = must[0].get("title", "")[:60]
    return f"今日主线：围绕《{title}》展开，建议从其问题设定和可复现实验切入。"


def deep_read_bucket_order(item: dict[str, Any]) -> int:
    section_id = item.get("primary_section", {}).get("id", "")
    if section_id in {"context_compression_memory", "context_compression", "context_memory"}:
        return 0
    if section_id in {"agents", "rl"}:
        return 1
    if section_id in {"model_distillation", "distillation_efficiency", "open_world_learning", "open_world", "cv"}:
        return 2
    return 9


def deep_read_sort_key(item: dict[str, Any]) -> tuple[int, int, float, float, str]:
    scores = item.get("scores", {})
    return (
        deep_read_bucket_order(item),
        -_mainline_priority_score(item),
        -scores.get("personal_score", 0.0),
        -scores.get("research_relevance", 0.0),
        item.get("title", ""),
    )


def build_overview(processed: dict[str, Any]) -> dict[str, Any]:
    items = processed.get("items", [])
    must = sorted([item for item in items if item.get("reading_tier") == "MUST_READ"], key=deep_read_sort_key)
    skim = [item for item in items if item.get("reading_tier") == "SKIM"]
    watch = [item for item in items if item.get("reading_tier") == "WATCH"]
    watch_display = sorted(watch, key=score_rank, reverse=True)[:12]
    tracked = must + skim
    if must:
        direction = section_title_from_item(must[0])
    else:
        section_counter = Counter(section_title_from_item(item) for item in tracked or items[:20])
        direction = section_counter.most_common(1)[0][0] if section_counter else "今日信号分散"
    must_titles = "；".join(item.get("title", "") for item in must[:3])
    skim_titles = "；".join(item.get("title", "") for item in skim[:5])
    watch_titles = "；".join(item.get("title", "") for item in watch_display[:5])
    keywords = top_keywords(tracked or items, limit=8)
    judgement = _generate_trend_judgement(must, direction)
    return {
        "most_important_direction": direction,
        "must_read_count": len(must),
        "must_read_titles": must_titles,
        "skim_count": len(skim),
        "skim_titles": skim_titles,
        "watch_count": len(watch_display),
        "watch_titles": watch_titles,
        "keywords": keywords,
        "judgement": judgement,
    }



def reading_purpose(item: dict[str, Any]) -> str:
    section_id = item.get("primary_section", {}).get("id", "")
    if section_id in {"context_compression_memory", "context_compression", "context_memory"}:
        return "判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。"
    if section_id == "agents":
        return "提取 Agent 任务设定、工具使用方式、规划机制和评测指标。"
    if section_id in {"open_world_learning", "open_world"}:
        return "关注开放集/OOD/持续学习设定与可复用 benchmark。"
    if section_id in {"model_distillation", "distillation_efficiency"}:
        return "评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。"
    if item.get("is_open_source_project"):
        return "判断代码质量、复现实验入口和是否值得 clone 研读。"
    return "判断该成果与当前研究问题的连接点和是否值得进入文献库。"


def is_eligible_for_deep_read(item: dict[str, Any]) -> bool:
    """
    判断条目是否符合深读清单的要求：
    1. 必须是论文、技术报告或高质量一手研究 blog
    2. 不得是 GitHub / Open Source Projects 分类
    3. grounding_level 不能是 title_only
    """
    if item.get("is_open_source_project"):
        return False
    
    section_title = item.get("primary_category", {}).get("title", "")
    if section_title == "GitHub / Open Source Projects":
        return False
    
    ground_level = grounding_level(item)
    if ground_level == "title_only":
        return False
    
    source_type = str(item.get("source", {}).get("type", "")).lower()
    valid_types = {"arxiv", "openreview", "hf_daily_papers", "hf_papers_page"}
    
    kind = item.get("source", {}).get("kind", "")
    is_primary = kind == "primary"
    
    if source_type in valid_types or is_primary:
        return True
    
    return False


def _mainline_priority_score(item: dict[str, Any]) -> int:
    title = item.get("title", "").lower()
    summary = item.get("summary", "").lower()
    text = title + " " + summary
    section_id = item.get("primary_section", {}).get("id", "")
    
    priority_keywords = [
        ("stale", 10),
        ("memory valid", 9),
        ("memory staleness", 9),
        ("strata", 8),
        ("context compression", 8),
        ("context memory", 7),
        ("long context", 7),
        ("dinorankclip", 6),
        ("ranking clip", 6),
        ("dino clip", 6),
        ("agent", 5),
        ("planning", 4),
        ("reasoning", 4),
        ("distillation", 3),
        ("vlm", 3),
        ("vision language", 3),
    ]
    
    score = 0
    for keyword, priority in priority_keywords:
        if keyword in text:
            score += priority
    
    section_priority = {
        "context_compression_memory": 10,
        "context_compression": 9,
        "context_memory": 8,
        "agents": 7,
        "model_distillation": 6,
        "open_world_learning": 5,
    }
    score += section_priority.get(section_id, 0)
    
    return score


def render_deep_read_list(items: list[dict[str, Any]]) -> str:
    must_candidates = [item for item in items if item.get("reading_tier") == "MUST_READ"]
    eligible = [item for item in must_candidates if is_eligible_for_deep_read(item)]
    
    eligible.sort(key=deep_read_sort_key)
    eligible = eligible[:3]
    
    if not eligible:
        return "- 今日没有符合条件的深读条目。"
    
    return "\n".join(
        f"- [{item.get('title')}]({item.get('url')})：预计阅读目的：{reading_purpose(item)}"
        for item in eligible
    )


def render_classic_revisit(classics: list[dict[str, Any]]) -> str:
    if not classics:
        return "- 今日没有足够明确的主题连接，暂不推荐经典论文。"
    lines: list[str] = []
    for idx, paper in enumerate(classics[:3], 1):
        related_sections = "、".join(paper.get("related_sections", [])) or "相关方向"
        authors = "、".join(str(author) for author in paper.get("authors", [])[:8])
        if len(paper.get("authors", [])) > 8:
            authors += " 等"
        topic_tags = "、".join(str(tag) for tag in paper.get("topic_tags", [])[:8])
        lines.append(f"### {idx}. [{paper.get('title')}]({paper.get('url')})（{paper.get('year')}）")
        lines.append(f"- 作者：{authors or '未知'}")
        lines.append(f"- topic_tags：{topic_tags or '未标注'}")
        lines.append(f"- 关联方向：{related_sections}")
        lines.append(f"- 为什么经典：{paper.get('why_classic') or paper.get('why_now')}")
        concept = paper.get("concept_connection") or {}
        if concept:
            lines.append(f"- 今日新论文继承了什么问题：{concept.get('inherits', '需要打开今日论文确认。')}")
            lines.append(f"- 它挑战了什么经典假设：{concept.get('challenges', '需要打开今日论文确认。')}")
            lines.append(f"- 它推进到什么新场景：{concept.get('extends', '需要打开今日论文确认。')}")
        else:
            lines.append(f"- 它和今日新论文的概念连接：{paper.get('modern_connection', '今天没有足够明确的新论文连接；作为基础脉络复习。')}")
        if paper.get("prerequisite"):
            lines.append(f"- 预备知识：{paper.get('prerequisite')}")
        related_today = paper.get("related_today", [])
        if related_today:
            lines.append("- 相关今日条目：")
            for item in related_today:
                terms = "、".join(item.get("connection_terms", []))
                suffix = f"；连接词：{terms}" if terms else ""
                lines.append(f"  - [{item.get('title')}]({item.get('url')})（{item.get('section')}{suffix}）")
        lines.append("")
    return "\n".join(lines).rstrip()


def previous_report_link(report_date: str) -> str:
    try:
        previous = datetime.strptime(report_date, "%Y-%m-%d") - timedelta(days=1)
    except ValueError:
        return "未知"
    previous_date = previous.strftime("%Y-%m-%d")
    previous_path = Path("reports") / "daily" / previous.strftime("%Y") / previous.strftime("%m") / f"{previous_date}.md"
    return str(previous_path).replace("\\", "/") if previous_path.exists() else f"{previous_date}：未找到上一期日报"


def format_count_map(value: Any) -> str:
    if not isinstance(value, dict) or not value:
        return "none"
    return ", ".join(f"{key}:{count}" for key, count in sorted(value.items()))


def llm_runtime_stats() -> dict[str, Any]:
    global LLM_SUMMARY_CALLS

    try:
        from models.client import llm_stats_snapshot

        stats = llm_stats_snapshot()
    except Exception:
        stats = {}

    api_requests_total = int(stats.get("api_requests_total") or 0)
    LLM_SUMMARY_CALLS = api_requests_total
    return {
        "llm_items_processed": LLM_ITEMS_PROCESSED,
        "role_pipeline_items": ROLE_PIPELINE_ITEMS,
        "single_llm_items": SINGLE_LLM_ITEMS,
        "api_requests_total": api_requests_total,
        "api_requests_by_provider": format_count_map(stats.get("api_requests_by_provider")),
        "api_requests_by_role": format_count_map(stats.get("api_requests_by_role")),
        "cache_hits": int(stats.get("cache_hits") or 0),
        "cache_misses": int(stats.get("cache_misses") or 0),
        "last_llm_error": LAST_LLM_ERROR or stats.get("last_model_error") or "none",
        "provider_disabled": stats.get("provider_disabled") or "none",
        "provider_disabled_reason": stats.get("provider_disabled_reason") or "none",
        "daily_llm_budget_rmb": stats.get("daily_llm_budget_rmb") if stats.get("daily_llm_budget_rmb") is not None else 1.0,
        "estimated_llm_cost_rmb": stats.get("estimated_llm_cost_rmb") if stats.get("estimated_llm_cost_rmb") is not None else 0.0,
        "estimated_input_tokens": stats.get("estimated_input_tokens") or 0,
        "estimated_output_tokens": stats.get("estimated_output_tokens") or 0,
        "cost_guard_blocked_calls": stats.get("cost_guard_blocked_calls") or 0,
        "cost_guard_enabled": stats.get("cost_guard_enabled") if stats.get("cost_guard_enabled") is not None else True,
    }


def build_template_context(processed: dict[str, Any], report_date: str, report_path: Path) -> dict[str, Any]:
    items = processed.get("items", [])
    prepare_llm_plan(items)
    collection_time = processed.get("generated_at") or datetime.now().isoformat(timespec="seconds")
    benchmark_appendix = write_benchmark_appendix(processed, report_date)
    backend = active_summary_backend()
    llm_enabled = backend.get("provider") != "local" and backend.get("summary_mode") != "local"
    overview = build_overview(processed)
    primary = {
        "context_compression": render_primary_section(processed, ["context_compression_memory", "context_compression", "context_memory"]),
        "agents": render_primary_section(processed, ["agents"]),
        "open_world_learning": render_primary_section(processed, ["open_world_learning", "open_world"]),
        "model_distillation": render_primary_section(processed, ["model_distillation", "distillation_efficiency"]),
    }
    traditional = {
        "cv": render_traditional_section(processed, "cv"),
        "nlp": render_traditional_section(processed, "nlp"),
        "rl": render_traditional_section(processed, "rl"),
        "model_architecture": render_traditional_section(processed, "model_architecture"),
        "learning_methods": render_traditional_section(processed, "learning_methods"),
    }
    other_highlights = render_other_section(processed, ["highlights", "other_highlights"], limit=5)
    benchmark_evaluation = render_benchmark_section(processed, report_date=report_date)
    github_projects = "\n".join(render_github_projects(processed.get("github_projects", [])))
    institutional_updates = render_other_section(processed, ["institutional_updates"], limit=5)
    awards_notable_papers = render_awards_notable_papers(processed)
    university_lab_radar = render_university_lab_radar(processed, report_date=report_date)
    context_community_signals = render_context_community_signals(processed)
    classic_revisit = render_classic_revisit(processed.get("classic_revisit", []))
    deep_read_list = render_deep_read_list(items)
    runtime_stats = llm_runtime_stats()
    return {
        "report_date": report_date,
        "overview": overview,
        "primary": primary,
        "traditional": traditional,
        "other_highlights": other_highlights,
        "benchmark_evaluation": benchmark_evaluation,
        "github_projects": github_projects,
        "institutional_updates": institutional_updates,
        "awards_notable_papers": awards_notable_papers,
        "university_lab_radar": university_lab_radar,
        "context_community_signals": context_community_signals,
        "classic_revisit": classic_revisit,
        "deep_read_list": deep_read_list,
        "collection": {
            "generated_at": collection_time,
            "source_count": source_count(processed),
            "source_health": render_source_health(processed),
            "raw_count": processed.get("counts", {}).get("raw", 0),
            "dedup_count": processed.get("counts", {}).get("deduped", 0),
            "summary_mode": backend.get("summary_mode", "local"),
            "provider": backend.get("provider", "local"),
            "model": backend.get("model", "local fallback"),
            "roles": backend.get("roles", ""),
            "llm_summary_calls": runtime_stats["api_requests_total"],
            "llm_items_processed": runtime_stats["llm_items_processed"],
            "role_pipeline_items": runtime_stats["role_pipeline_items"],
            "single_llm_items": runtime_stats["single_llm_items"],
            "api_requests_total": runtime_stats["api_requests_total"],
            "api_requests_by_provider": runtime_stats["api_requests_by_provider"],
            "api_requests_by_role": runtime_stats["api_requests_by_role"],
            "cache_hits": runtime_stats["cache_hits"],
            "cache_misses": runtime_stats["cache_misses"],
            "last_llm_error": runtime_stats["last_llm_error"],
            "provider_disabled": runtime_stats["provider_disabled"],
            "provider_disabled_reason": runtime_stats["provider_disabled_reason"],
            "daily_llm_budget_rmb": runtime_stats["daily_llm_budget_rmb"],
            "estimated_llm_cost_rmb": runtime_stats["estimated_llm_cost_rmb"],
            "estimated_input_tokens": runtime_stats["estimated_input_tokens"],
            "estimated_output_tokens": runtime_stats["estimated_output_tokens"],
            "cost_guard_blocked_calls": runtime_stats["cost_guard_blocked_calls"],
            "cost_guard_enabled": runtime_stats["cost_guard_enabled"],
            "llm_zero_call_warning": (
                "API key configured but no LLM summary calls were made; check budget, cache, grounding, or provider errors."
                if has_any_llm_api_key() and runtime_stats["api_requests_total"] == 0 and llm_enabled
                else ""
            ),
            "local_summary_notice": "" if llm_enabled else "No API key was available; generated deterministic local fallback summaries.",
            "benchmark_appendix": benchmark_appendix,
            "report_path": str(report_path).replace("\\", "/"),
            "previous_report_link": previous_report_link(report_date),
        },
    }


def render_daily_template(context: dict[str, Any], template_path: str | Path = DEFAULT_TEMPLATE_PATH) -> str:
    path = Path(template_path)
    env = Environment(
        loader=FileSystemLoader(str(path.parent)),
        autoescape=False,
        trim_blocks=False,
        lstrip_blocks=True,
    )
    template = env.get_template(path.name)
    return template.render(**context).rstrip() + "\n"


def generate_report(
    processed: dict[str, Any] | list[dict[str, Any]],
    output: str | Path,
    *,
    report_date: str | None = None,
    latest_path: str | Path | None = "report.md",
    archive_latest: bool = True,
    generate_html: bool = True,
) -> str:
    if isinstance(processed, list):
        processed = {
            "date": report_date or datetime.now().strftime("%Y-%m-%d"),
            "counts": {"processed": len(processed)},
            "sections": [{"title": "Legacy Ranked Items", "group": "core_focus", "items": processed}],
            "github_projects": [],
            "classic_revisit": [],
            "items": processed,
        }

    report_date = report_date or processed.get("date") or datetime.now().strftime("%Y-%m-%d")
    output_path = Path(output)
    
    # Archive previous latest.md before overwriting
    if archive_latest and latest_path and Path(latest_path).exists():
        archive_report_with_timestamp(
            latest_path,
            archive_dir="reports/history",
            suffix="latest",
        )

    # Generate new report
    context = build_template_context(processed, report_date, output_path)
    rendered = render_daily_template(context)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")

    # Archive the newly generated report (LLM summary version)
    archive_report_with_timestamp(
        output_path,
        archive_dir="reports/history",
        suffix="daily",
    )

    if latest_path:
        shutil.copyfile(output_path, latest_path)

    # Auto-generate HTML from the generated Markdown
    if generate_html:
        try:
            html_path = generate_html_report(output_path)
            print(f"Generated HTML report: {html_path}")

            # Also generate HTML for report.md (root level) as index.html for GitHub Pages
            if latest_path and Path(latest_path).exists():
                root_html_path = Path("index.html")
                generate_html_report(latest_path, root_html_path)
                print(f"Generated root HTML report: {root_html_path}")
        except Exception as e:
            print(f"HTML generation warning: {e}")

    return rendered


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Chinese Markdown dashboard report.")
    parser.add_argument("--input", default="data/processed.json")
    parser.add_argument("--output", default=None)
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"))
    args = parser.parse_args()

    output = args.output or f"reports/daily/{args.date[:4]}/{args.date[5:7]}/{args.date}.md"
    processed = load_json(args.input)
    generate_report(processed, output, report_date=args.date)
    print(f"wrote report to {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
