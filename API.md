# 多模型协作 API 文档

## Author: 陈子聪 (Chen Zicong)
## Date: 2026-05-10
## Purpose: 详细说明多模型协作的两阶段工作机制和综合流程

---

## 目录

1. [整体架构](#1-整体架构)
2. [配置加载流程](#2-配置加载流程)
3. [两阶段协作流程](#3-两阶段协作流程)
4. [Stage 1: 多模型独立生成](#4-stage-1-多模型独立生成)
5. [Stage 2: Editor Model 综合](#5-stage-2-editor-model-综合)
6. [投票机制详解](#6-投票机制详解)
7. [返回字段说明](#7-返回字段说明)
8. [容错处理](#8-容错处理)

---

## 1. 整体架构

```
用户请求 (python run.py)
       ↓
  run.py (入口)
       ↓
  load_dotenv() 加载 .env 环境变量
       ↓
  summarize.py::summarize_item()
       ↓
  ensemble_enabled() 检查 MODEL_MODE
       ↓
  get_ensemble_model() 获取协作引擎
       ↓
  ┌─────────────────────────────────────────────────────────────┐
  │              EnsembleModel.summarize()                       │
  │                                                             │
  │  ┌───────────────────────────────────────────────────────┐  │
  │  │              Stage 1: 多模型独立生成                    │  │
  │  │                                                       │  │
  │  │  ┌──────────┐  ┌──────────┐  ┌─────┐                │  │
  │  │  │ DeepSeek │  │  Kimi   │  │GLM  │                │  │
  │  │  │  Model   │  │  Model  │  │Model│                │  │
  │  │  └────┬─────┘  └────┬─────┘  └──┬──┘                │  │
  │  │       │             │            │                    │  │
  │  │       ↓             ↓            ↓                    │  │
  │  │  结构化摘要 + 置信度 + 幻觉风险评估                    │  │
  │  └─────────────→ 汇总结果 ◀─────────────────────────────┘  │
  │                        ↓                                   │
  │  ┌───────────────────────────────────────────────────────┐  │
  │  │              Stage 2: Editor Model 综合               │  │
  │  │                                                       │  │
  │  │  ┌─────────────────────────────────────────────────┐  │  │
  │  │  │  结构化字段 → 投票 (primary_category, tier,      │  │  │
  │  │  │             suggested_action, is_benchmark...)  │  │  │
  │  │  └─────────────────────────────────────────────────┘  │  │
  │  │                         ↓                             │  │
  │  │  ┌─────────────────────────────────────────────────┐  │  │
  │  │  │  自然语言字段 → Editor Model 综合生成统一摘要     │  │  │
  │  │  │  (what_is_it, problem, method_or_contribution,  │  │  │
  │  │  │   why_important, deep_read)                     │  │  │
  │  │  └─────────────────────────────────────────────────┘  │  │
  │  └─────────────→ 最终摘要 ◀─────────────────────────────┘  │
       ↓
  normalize_summary() 标准化
       ↓
  生成报告
```

---

## 2. 配置加载流程

### 2.1 环境变量加载

**文件**: `run.py`

```python
from dotenv import load_dotenv
load_dotenv()  # 自动加载 .env 文件
```

**`.env` 文件内容示例**:
```env
MODEL_MODE=ensemble
DEEPSEEK_API_KEY=sk-xxx
KIMI_API_KEY=sk-xxx
GLM_API_KEY=xxx
OPENAI_API_KEY=sk-xxx
OPENAI_BASE_URL=https://api.openai.com/v1
ENSEMBLE_STRATEGY=editor
```

### 2.2 模型配置加载

**文件**: `summarize.py` → `load_model_config()`

```python
def load_model_config() -> dict[str, Any]:
    config_path = Path("config") / "models.yaml"
    config = yaml.safe_load(config_path)
    
    for model in config.get("models", []):
        api_key_env = model.get("api_key", "")
        if api_key_env.startswith("${") and api_key_env.endswith("}"):
            env_var = api_key_env[2:-1]
            model["api_key"] = os.getenv(env_var, "")
    
    return config
```

**`config/models.yaml` 内容**:
```yaml
mode: ensemble
strategy: editor

models:
  - type: deepseek
    name: deepseek
    api_key: ${DEEPSEEK_API_KEY}
    base_url: https://api.deepseek.com
    model: deepseek-v4-flash
    weight: 1.0

  - type: kimi
    name: kimi
    api_key: ${KIMI_API_KEY}
    base_url: https://api.moonshot.cn/v1
    model: moonshot-v1-8k
    weight: 1.0

  - type: glm
    name: glm
    api_key: ${GLM_API_KEY}
    base_url: https://open.bigmodel.cn/api/paas/v4
    model: glm-4.7-flash
    weight: 1.0

editor:
  enabled: true
  api_key: ${OPENAI_API_KEY}
  base_url: ${OPENAI_BASE_URL}
  model: gpt-4o-mini
```

---

## 3. 两阶段协作流程

### 3.1 流程概述

两阶段流程解决了传统 exact match voting 的根本问题：不同模型几乎不会生成完全相同的自然语言摘要。

| 阶段 | 职责 | 输出 |
|------|------|------|
| **Stage 1** | 多模型独立生成结构化摘要 | 每个模型输出完整结构化字段 + 置信度 + 幻觉风险 |
| **Stage 2** | Editor Model 综合 | 结构化字段投票 + 自然语言字段综合生成 |

### 3.2 字段分工

**可投票字段（结构化字段）**:
- `primary_category` - 主要分类
- `reading_tier` - 阅读层级
- `suggested_action` - 建议行动
- `is_benchmark` - 是否基准测试
- `is_open_source_project` - 是否开源项目

**Editor 综合字段（自然语言字段）**:
- `what_is_it` - 这是什么？
- `problem` - 解决了什么问题？
- `method_or_contribution` - 方法或贡献是什么？
- `why_important` - 为什么对我重要？
- `deep_read` - 是否建议深读？

---

## 4. Stage 1: 多模型独立生成

### 4.1 单模型调用

每个模型（DeepSeek/Kimi/GLM）独立生成结构化摘要：

**文件**: `models/deepseek.py` → `DeepSeekModel.summarize()`

```python
def summarize(self, item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    prompt = self._build_prompt(item)
    
    response = requests.post(
        f"{self.base_url}/chat/completions",
        headers={
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": self.model_name,
            "messages": [
                {"role": "system", "content": self._system_prompt()},
                {"role": "user", "content": json.dumps(prompt)}
            ],
            "temperature": 0.2,
            "response_format": {"type": "json_object"},
        },
        timeout=60
    )
    
    parsed = json.loads(response.json()["choices"][0]["message"]["content"])
    return self._validate_response(parsed)
```

### 4.2 Stage 1 输出结构

每个模型返回增强后的结果：

```python
{
    "what_is_it": "关于长上下文扩展的研究...",
    "problem": "解决了 LLM 上下文窗口受限的问题...",
    "method_or_contribution": "提出了新的位置编码方法...",
    "why_important": "与研究方向高度相关...",
    "deep_read": "建议深读...",
    "suggested_action": "read_pdf",
    "confidence": 0.85,           # 新增：置信度评分
    "potential_hallucination_risk": 0.15,  # 新增：幻觉风险评估
    "model_name": "deepseek",
    "model_weight": 1.0
}
```

### 4.3 置信度评估

**文件**: `models/ensemble.py` → `_estimate_confidence()`

```python
def _estimate_confidence(self, result: Dict[str, Any]) -> float:
    score = 0.0
    fields = ["what_is_it", "problem", "method_or_contribution", 
              "why_important", "deep_read"]
    
    for field in fields:
        value = result.get(field, "")
        if value and len(value) >= 10:
            score += 0.15  # 每个有效字段 +0.15
    
    if result.get("suggested_action") in {"read_pdf", "skim", "save", "ignore"}:
        score += 0.1  # 有效行动建议 +0.1
    
    return min(1.0, score)  # 归一化到 [0, 1]
```

### 4.4 幻觉风险评估

**文件**: `models/ensemble.py` → `_estimate_hallucination_risk()`

```python
def _estimate_hallucination_risk(self, result: Dict[str, Any]) -> float:
    risk = 0.0
    text = " ".join(str(result.get(f, "")) for f in EDITOR_FIELDS)
    
    if self._contains_suspicious_numbers(text):
        risk += 0.3  # 检测到可疑数字
    
    if self._contains_unsupported_claims(text):
        risk += 0.3  # 检测到无证据支持的断言
    
    if self._contains_boilerplate(text):
        risk += 0.2  # 检测到模板化套话
    
    return min(1.0, risk)
```

**风险检测模式**:

| 检测项 | 模式/关键词 | 风险增量 |
|--------|------------|---------|
| 可疑数字 | `\b\d{3,}\b`, `准确率 >= 95%` | +0.3 |
| 无证据断言 | "首次提出", "最先进", "革命性" | +0.3 |
| 模板套话 | "具有重要意义", "提供方向" | +0.2 |

---

## 5. Stage 2: Editor Model 综合

### 5.1 流程架构

```
Stage 1 结果 → 结构化字段投票 → 投票结果
              ↓
              Editor Model 输入构建
              ↓
              Editor Model 调用
              ↓
              自然语言字段综合
              ↓
              合并最终结果
```

### 5.2 Editor Model 输入

**文件**: `models/ensemble.py` → `_build_editor_input()`

```python
{
    "item": {
        "title": "LongRoPE: Extending LLM Context Beyond 2M Tokens",
        "abstract": "We propose LongRoPE...",
        "url": "https://arxiv.org/abs/2404.12345",
        "source": {"name": "arXiv", "kind": "primary"},
        "evidence_text": "完整证据文本（用于验证）"
    },
    "model_outputs": [
        {
            "what_is_it": "模型1的输出...",
            "problem": "...",
            "method_or_contribution": "...",
            "why_important": "...",
            "deep_read": "...",
            "model_name": "deepseek",
            "confidence": 0.85,
            "potential_hallucination_risk": 0.15
        },
        {
            "what_is_it": "模型2的输出...",
            ...
        }
    ],
    "required_fields": ["what_is_it", "problem", "method_or_contribution", 
                        "why_important", "deep_read"]
}
```

### 5.3 Editor Model 系统提示词

```
你是一位严谨的 AI Research Radar 编辑，负责综合多个 AI 模型的输出。

你的任务是：
1. 综合多个模型的共识，不简单复制任何单个模型的输出
2. 删除不被输入证据（evidence_text）支持的具体数字和结论
3. 用自然、具体、克制的中文写摘要，不营销，不编造
4. 如果多个模型观点不一致，取最保守、最有证据支持的结论
5. 如果信息不足，直接说明，不要编造

返回格式要求：
必须返回严格 JSON，字段必须且只能包含：
what_is_it, problem, method_or_contribution, why_important, deep_read

每个字段 1-2 句，尽量具体但不虚构细节。
```

### 5.4 结构化字段投票

**文件**: `models/ensemble.py` → `_vote_structured_fields()`

```python
def _vote_structured_fields(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
    final = {}
    VOTABLE_FIELDS = ["primary_category", "reading_tier", 
                      "suggested_action", "is_benchmark", "is_open_source_project"]
    
    for field in VOTABLE_FIELDS:
        values = [r.get(field) for r in results if r.get(field) is not None]
        if values:
            if field in ["is_benchmark", "is_open_source_project"]:
                final[field] = self._vote_boolean(values)  # 多数决定
            elif field == "suggested_action":
                final[field] = self._vote_action(values)    # 加权投票
            else:
                final[field] = self._vote_discrete(values)  # 简单多数
    
    return final
```

---

## 6. 投票机制详解

### 6.1 行动建议投票

**文件**: `models/ensemble.py` → `_vote_action()`

```python
action_order = {
    "read_pdf": 5,    # 最高优先级
    "reproduce": 4,   # 可复现
    "skim": 3,        # 快速浏览
    "save": 2,        # 保存
    "ignore": 1        # 忽略
}

def _vote_action(self, values):
    counter = Counter(values)
    best_action = "save"
    best_score = 0
    
    for action, count in counter.items():
        if action in action_order:
            score = count * action_order[action]
            if score > best_score:
                best_score = score
                best_action = action
    
    return best_action
```

**示例**:
```
投票: 2票 "skim", 1票 "read_pdf"
计算: skim = 2×3 = 6, read_pdf = 1×5 = 5
结果: "skim"
```

### 6.2 回退策略

当 Editor Model 不可用或失败时，回退到基于置信度的选择：

```python
def _select_best_text(self, values, results, field):
    best_value = ""
    best_score = 0.0
    
    for i, value in enumerate(values):
        confidence = results[i].get("confidence", 0.5)
        hallucination_risk = results[i].get("potential_hallucination_risk", 0.5)
        length_score = min(len(value) / 100, 1.0)
        
        score = confidence * (1 - hallucination_risk) * length_score
        
        if score > best_score:
            best_score = score
            best_value = value
    
    return best_value
```

---

## 7. 返回字段说明

### 7.1 Stage 1 单模型输出

| 字段 | 类型 | 说明 |
|------|------|------|
| `what_is_it` | str | 这是什么？ |
| `problem` | str | 解决了什么问题？ |
| `method_or_contribution` | str | 方法或贡献是什么？ |
| `why_important` | str | 为什么对我重要？ |
| `deep_read` | str | 是否建议深读？ |
| `suggested_action` | str | 建议行动 |
| `confidence` | float | 置信度 [0, 1] |
| `potential_hallucination_risk` | float | 幻觉风险 [0, 1] |
| `model_name` | str | 模型名称 |
| `model_weight` | float | 模型权重 |

### 7.2 Stage 2 最终输出

| 字段 | 类型 | 来源 |
|------|------|------|
| `what_is_it` | str | Editor Model |
| `problem` | str | Editor Model |
| `method_or_contribution` | str | Editor Model |
| `why_important` | str | Editor Model |
| `deep_read` | str | Editor Model |
| `primary_category` | str | 投票 |
| `reading_tier` | str | 投票 |
| `suggested_action` | str | 投票 |
| `is_benchmark` | bool | 投票 |
| `is_open_source_project` | bool | 投票 |

---

## 8. 容错处理

### 8.1 单模型失败不影响整体

```python
def _stage1_independent_summarize(self, item):
    results = []
    for model in self.models:
        try:
            result = model.summarize(item)
            if result:
                enriched_result = self._enrich_with_confidence(result, model)
                results.append(enriched_result)
        except Exception as e:
            print(f"Model {model.name} failed: {e}")
            # 单模型失败，继续调用其他模型
    
    return results
```

### 8.2 Editor Model 失败降级

```python
def _stage2_editor_synthesis(self, item, stage1_results):
    final = {}
    
    final.update(self._vote_structured_fields(stage1_results))
    
    editor_output = self._call_editor_model(...)
    
    if editor_output:
        for field in EDITOR_FIELDS:
            final[field] = editor_output.get(field, "")
    else:
        # Editor 失败，降级为基于置信度的选择
        final.update(self._fallback_synthesis(stage1_results))
    
    return final
```

### 8.3 所有模型失败

```python
def summarize(self, item):
    if not self.models:
        return None
    
    stage1_results = self._stage1_independent_summarize(item)
    
    if not stage1_results:
        return None  # 所有模型都失败
    
    # 继续 Stage 2...
```

---

## 9. 策略对比

| 策略 | 适用场景 | 特点 |
|------|---------|------|
| `editor` | 推荐 | 自然语言字段由 Editor 综合，结构化字段投票 |
| `voting` | 备选 | 所有字段简单多数投票（不推荐用于自然语言） |
| `weighted` | 备选 | 加权投票，考虑模型权重 |
| `consensus` | 保守 | 仅当所有模型一致时采用，否则降级 |

---

## 10. 性能考虑

| 因素 | 影响 |
|------|------|
| Stage 1 模型数量 | N模型 = N倍 API 调用时间 |
| Stage 2 Editor | +1 次 API 调用 |
| 网络延迟 | 每个模型约 1-3 秒 |
| Token 消耗 | (N+1) 倍输入 token |

**优化建议**:
- 使用轻量模型（如 `gpt-4o-mini`）作为 Editor
- 调整各模型权重平衡质量与成本
- 启用缓存避免重复处理相同条目

---

## 11. 故障排查

| 问题 | 可能原因 | 解决方案 |
|------|---------|---------|
| Editor 返回 None | API Key 无效或超时 | 检查 `OPENAI_API_KEY` 和网络 |
| 部分模型失败 | 平台服务异常 | 查看日志确认失败模型 |
| 摘要质量差 | Editor 输入不足 | 增加 evidence_text 长度 |
| 幻觉风险高 | 模型输出包含可疑内容 | 检查 Stage 1 置信度评分 |

---

*文档版本: 2.0*
*最后更新: 2026-05-10*
*变更说明: 重构为两阶段流程，自然语言字段由 Editor Model 综合生成*