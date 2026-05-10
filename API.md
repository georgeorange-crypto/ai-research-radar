# 多模型协作 API 文档

## Author: 陈子聪 (Chen Zicong)
## Date: 2026-05-10
## Purpose: 详细说明多模型协作的工作机制和投票流程

---

## 目录

1. [整体架构](#1-整体架构)
2. [配置加载流程](#2-配置加载流程)
3. [API 调用流程](#3-api-调用流程)
4. [投票机制详解](#4-投票机制详解)
5. [返回字段说明](#5-返回字段说明)
6. [容错处理](#6-容错处理)

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
  ┌─────────────────────────────────────┐
  │        EnsembleModel.summarize()      │
  │                                      │
  │  ┌──────────┐  ┌──────────┐  ┌─────┐ │
  │  │ DeepSeek │  │  Kimi   │  │GLM  │ │
  │  │  Model   │  │  Model  │  │Model│ │
  │  └────┬─────┘  └────┬─────┘  └──┬──┘ │
  │       │             │            │     │
  │       └─────────────┼────────────┘     │
  │                     ↓                  │
  │              投票/加权/共识             │
  │                     ↓                  │
  └─────────────→ 最终摘要 ◀─────────────┘
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
ENSEMBLE_STRATEGY=voting
```

### 2.2 模型配置加载

**文件**: `summarize.py` → `load_model_config()`

```python
def load_model_config() -> dict[str, Any]:
    config_path = Path("config") / "models.yaml"
    config = yaml.safe_load(config_path)
    
    # 替换环境变量 ${VAR_NAME} 为实际值
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
strategy: voting  # voting | weighted | consensus

models:
  - type: deepseek
    name: deepseek
    api_key: ${DEEPSEEK_API_KEY}  # 自动替换为环境变量
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
```

---

## 3. API 调用流程

### 3.1 单模型调用

每个模型（DeepSeek/Kimi/GLM）都遵循相同的调用模式。以 DeepSeek 为例：

**文件**: `models/deepseek.py` → `DeepSeekModel.summarize()`

```python
def summarize(self, item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    # 1. 构建提示词
    prompt = self._build_prompt(item)
    
    # 2. 调用 API
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
    
    # 3. 解析响应
    parsed = json.loads(response.json()["choices"][0]["message"]["content"])
    
    # 4. 验证返回字段
    return self._validate_response(parsed)
```

### 3.2 提示词结构

```python
{
    "title": "论文/项目标题",
    "source": {"name": "来源名称", "kind": "primary|aggregator|media"},
    "url": "https://...",
    "abstract_or_excerpt": "摘要内容（前1800字符）",
    "primary_section": {"id": "context_compression", "title": "上下文压缩"},
    "reading_tier": "MUST_READ | SKIM | ARCHIVE | IGNORE",
    "matched_focus_areas": ["长上下文", "Agent"],
    "matched_keywords": ["RAG", "检索增强"],
    "scores": {
        "personal_score": 0.85,
        "global_score": 0.72,
        ...
    },
    "is_open_source_project": false,
    "required_fields": {
        "what_is_it": "这是什么？",
        "problem": "解决了什么问题？",
        ...
    }
}
```

### 3.3 System Prompt

所有模型使用相同的系统提示词：

```
你是严谨的 AI research radar 编辑，面向一位关注长上下文、Agent、开放世界学习和模型压缩的研究者。
用自然、具体、克制的中文写摘要，不营销，不编造，不重复套话。
只基于输入信息；信息不足时直接说明需要打开原文确认。
避免模板化表达，不要按来源类型写泛泛的跟踪价值判断。
返回严格 JSON，字段必须且只能包含：
what_is_it, problem, method_or_contribution, why_important, deep_read, suggested_action。
suggested_action 只能是 read_pdf、skim、save、reproduce、ignore 之一。
每个字段 1-2 句，尽量指出具体方法名、任务、数据、系统或实验线索。
```

---

## 4. 投票机制详解

### 4.1 策略选择

**文件**: `models/ensemble.py`

```python
if self.strategy == "voting":
    return self._vote_summary(results)
elif self.strategy == "weighted":
    return self._weighted_summary(results)
elif self.strategy == "consensus":
    return self._consensus_summary(results)
```

### 4.2 策略 1: 简单多数投票 (voting)

**原理**: 每个模型的每个字段独立投票，得票最多的选项获胜。

```
场景: 3个模型对 "suggested_action" 字段投票
- DeepSeek → "read_pdf"
- Kimi → "read_pdf"
- GLM → "skim"

结果: "read_pdf" (2票 vs 1票)
```

**代码实现**:

```python
def _vote_summary(self, results):
    final = {}
    fields = ["what_is_it", "problem", "method_or_contribution", 
              "why_important", "deep_read", "suggested_action"]
    
    for field in fields:
        values = [r[1].get(field, "") for r in results]
        
        if field == "suggested_action":
            final[field] = self._vote_action(values)  # 智能投票
        else:
            final[field] = self._vote_text(values)    # 简单多数
    
    return final

def _vote_text(self, values):
    counter = Counter(values)
    return counter.most_common(1)[0][0]  # 返回出现最多的文本
```

### 4.3 策略 2: 加权投票 (weighted)

**原理**: 根据模型的 `weight` 权重调整投票影响力。

```
场景: 权重配置 DeepSeek=2.0, Kimi=1.0, GLM=1.0
- DeepSeek → "read_pdf" (权重 2.0)
- Kimi → "read_pdf" (权重 1.0)
- GLM → "skim" (权重 1.0)

计算: "read_pdf" 得票 = 2.0 + 1.0 = 3.0
      "skim" 得票 = 1.0

结果: "read_pdf"
```

**代码实现**:

```python
def _weighted_summary(self, results):
    final = {}
    for field in fields:
        weighted_values = []
        for model, result in results:
            value = result.get(field, "")
            # 根据权重扩展投票次数
            weighted_values.extend([value] * int(model.weight * 10))
        
        if field == "suggested_action":
            final[field] = self._vote_action(weighted_values)
        else:
            final[field] = self._vote_text(weighted_values)
    
    return final
```

### 4.4 策略 3: 共识模式 (consensus)

**原理**: 只有当所有模型都给出相同答案时才采用，否则降级为投票。

```
场景:
- DeepSeek → "read_pdf"
- Kimi → "read_pdf"
- GLM → "skim"

分析: 不是所有模型都一致
结果: 降级为投票 → "read_pdf"

场景2:
- DeepSeek → "read_pdf"
- Kimi → "read_pdf"
- GLM → "read_pdf"

分析: 所有模型完全一致
结果: "read_pdf" (直接采用)
```

**代码实现**:

```python
def _consensus_summary(self, results):
    final = {}
    for field in fields:
        values = [r[1].get(field, "") for r in results]
        
        # 只有当所有模型都返回了结果且答案相同时才采用
        if len(values) >= len(self.models):
            unique_values = set(values)
            if len(unique_values) == 1:
                final[field] = values[0]  # 全票一致，直接采用
            else:
                final[field] = self._vote_text(values)  # 降级投票
        else:
            # 有模型失败，降级为投票
            final[field] = self._vote_text(values)
    
    return final
```

### 4.5 行动建议投票 (_vote_action)

对于 `suggested_action` 字段，采用加权评分机制：

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
            # 分数 = 得票数 × 行动优先级
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

---

## 5. 返回字段说明

每个模型返回的摘要包含 6 个字段：

| 字段 | 说明 | 示例 |
|------|------|------|
| `what_is_it` | 这是什么？ | "关于 RAG 系统长上下文处理的研究" |
| `problem` | 解决了什么问题？ | "解决了长文档检索效率低下的问题" |
| `method_or_contribution` | 方法或贡献是什么？ | "提出了一种层次化检索+重排的方案" |
| `why_important` | 为什么对我重要？ | "与你的长上下文研究方向高度相关" |
| `deep_read` | 是否建议深读？ | "建议深读，特别是检索部分的设计" |
| `suggested_action` | 建议行动 | `read_pdf` / `skim` / `save` / `reproduce` / `ignore` |

---

## 6. 容错处理

### 6.1 单模型失败不影响整体

```python
def summarize(self, item):
    results = []
    for model in self.models:
        try:
            result = model.summarize(item)
            if result:
                results.append((model, result))
        except Exception as e:
            print(f"Model {model.name} failed: {e}")
            # 单模型失败，继续调用其他模型
    
    if not results:
        return None  # 所有模型都失败才返回 None
    
    # 继续投票流程
    return self._vote_summary(results)
```

### 6.2 降级策略

当模型返回格式不正确时：

```python
def _validate_response(self, parsed):
    required = {"what_is_it", "problem", "method_or_contribution", 
               "why_important", "deep_read", "suggested_action"}
    
    if all(key in parsed for key in required):
        return parsed
    return None  # 格式不正确，视为失败
```

---

## 7. 完整调用示例

### 7.1 单条论文摘要生成

```python
# 1. 初始化
from summarize import get_ensemble_model

# 2. 获取协作引擎（自动加载配置和环境变量）
ensemble = get_ensemble_model()

# 3. 准备论文数据
item = {
    "title": "LongRoPE: Extending LLM Context Beyond 2M Tokens",
    "source": {"name": "arXiv", "kind": "primary"},
    "url": "https://arxiv.org/abs/2404.12345",
    "summary": "We propose LongRoPE, a method to extend the context window...",
    "reading_tier": "MUST_READ",
    "scores": {"personal_score": 0.92, "global_score": 0.88}
}

# 4. 生成协作摘要
result = ensemble.summarize(item)

# 5. 结果（投票后的最终摘要）
print(result)
# {
#     "what_is_it": "LongRoPE 是一种长上下文扩展方法...",
#     "problem": "LLM 在处理超长文本时受限...",
#     "method_or_contribution": "通过渐进式微调实现 2M+ 上下文...",
#     "why_important": "与你的长上下文研究方向直接相关...",
#     "deep_read": "建议深读，重点关注位置编码部分...",
#     "suggested_action": "read_pdf"
# }
```

### 7.2 批量论文排序

```python
# 1. 获取多条论文
items = [item1, item2, item3, ...]

# 2. 多模型协作排序
ranked = ensemble.rank(items)

# 3. 返回排序后的列表（综合三个模型的评分）
# Borda 计数: 排名第1得N分，排名第2得N-1分...
# 最终按综合得分排序
```

---

## 8. 性能考虑

| 因素 | 影响 |
|------|------|
| 模型数量 | 3模型 = 3倍API调用时间 |
| 网络延迟 | 每个模型约 1-3 秒 |
| Token 消耗 | 3模型 = 3倍输入token |
| 成本 | 取决于各模型定价 |

**优化建议**:
- 使用 `moonshot-v1-8k` 等轻量模型降低成本
- 调整 `OPENAI_SUMMARY_BUDGET` 限制调用次数
- 使用 `flash` 系列模型加速

---

## 9. 故障排查

| 问题 | 可能原因 | 解决方案 |
|------|---------|---------|
| 所有模型返回 None | API Key 无效或过期 | 检查 `.env` 中的 API Keys |
| 部分模型失败 | 该平台服务异常 | 查看日志确认是哪个模型失败 |
| 返回格式错误 | 模型输出不符合预期 | 检查 `models.yaml` 中的 `weight` 配置 |
| 投票结果不理想 | 模型观点分歧大 | 尝试 `consensus` 策略 |

---

*文档版本: 1.0*
*最后更新: 2026-05-10*
