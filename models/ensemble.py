from .base import BaseModel
from .client import ChatModelClient, log_model_error
from .summary_model import ACTION_CHOICES
from typing import Any, Dict, List, Optional
from collections import Counter
import json


class EnsembleModel(BaseModel):
    """多模型协作决策引擎 - 两阶段流程"""
    
    STRATEGIES = ["voting", "weighted", "consensus", "editor"]
    
    VOTABLE_FIELDS = ["suggested_action"]
    
    EDITOR_FIELDS = [
        "what_is_it",
        "problem",
        "method_or_contribution",
        "why_important",
        "deep_read"
    ]
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.strategy = config.get("strategy", "editor")
        self.models = self._load_models()
        self.editor_model = self._load_editor_model(config)
    
    def _load_models(self) -> List[BaseModel]:
        """动态加载配置的模型"""
        models = []
        for model_config in self.config.get("models", []):
            model_type = model_config.get("type")
            try:
                if model_type == "deepseek":
                    from .deepseek import DeepSeekModel
                    models.append(DeepSeekModel(model_config))
                elif model_type == "kimi":
                    from .kimi import KimiModel
                    models.append(KimiModel(model_config))
                elif model_type == "glm":
                    from .glm import GLMModel
                    models.append(GLMModel(model_config))
            except Exception as e:
                print(f"Failed to load model {model_type}: {e}")
        return models
    
    def _load_editor_model(self, config: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """加载 editor model 配置"""
        editor_config = config.get("editor", {})
        if editor_config.get("enabled", False):
            return editor_config
        return None
    
    def summarize(self, item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """两阶段多模型协作生成摘要"""
        if not self.models:
            return None
        
        stage1_results = self._stage1_independent_summarize(item)
        
        if not stage1_results:
            return None
        
        final = {}
        
        if self.strategy == "editor" and self.editor_model:
            final = self._stage2_editor_synthesis(item, stage1_results)
        else:
            final = self._stage2_voting_synthesis(stage1_results)
        
        return final
    
    def _stage1_independent_summarize(self, item: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Stage 1: 多模型独立生成结构化摘要"""
        results = []
        
        for model in self.models:
            try:
                result = model.summarize(item)
                if result:
                    enriched_result = self._enrich_with_confidence(result, model)
                    results.append(enriched_result)
            except Exception as e:
                print(f"Model {model.name} failed: {e}")
        
        return results
    
    def _enrich_with_confidence(self, result: Dict[str, Any], model: BaseModel) -> Dict[str, Any]:
        """为单模型结果添加置信度和幻觉风险评估"""
        result = result.copy()
        
        confidence = self._estimate_confidence(result)
        hallucination_risk = self._estimate_hallucination_risk(result)
        
        result.update({
            "confidence": confidence,
            "potential_hallucination_risk": hallucination_risk,
            "model_name": model.name,
            "model_weight": model.weight
        })
        
        return result
    
    def _estimate_confidence(self, result: Dict[str, Any]) -> float:
        """基于输出质量估算置信度"""
        score = 0.0
        fields = self.EDITOR_FIELDS
        
        for field in fields:
            value = result.get(field, "")
            if value and len(value) >= 10:
                score += 0.15
        
        if result.get("suggested_action") in ACTION_CHOICES:
            score += 0.1
        
        return min(1.0, score)
    
    def _estimate_hallucination_risk(self, result: Dict[str, Any]) -> float:
        """估算幻觉风险"""
        risk = 0.0
        text = " ".join(str(result.get(f, "")) for f in self.EDITOR_FIELDS)
        
        if self._contains_suspicious_numbers(text):
            risk += 0.3
        
        if self._contains_unsupported_claims(text):
            risk += 0.3
        
        if self._contains_boilerplate(text):
            risk += 0.2
        
        return min(1.0, risk)
    
    def _contains_suspicious_numbers(self, text: str) -> bool:
        """检测可疑数字（可能是编造的）"""
        import re
        patterns = [
            r"\b\d{3,}\b",
            r"\b\d+\.\d{2,}\b",
            r"\b(准确率|精度|效果|性能)\s*[>=]\s*\d+%?"
        ]
        for pattern in patterns:
            if re.search(pattern, text):
                return True
        return False
    
    def _contains_unsupported_claims(self, text: str) -> bool:
        """检测无证据支持的断言"""
        unsupported_phrases = [
            "首次提出",
            "最先进",
            "革命性",
            "突破",
            "里程碑",
            "超越所有现有方法"
        ]
        return any(phrase in text for phrase in unsupported_phrases)
    
    def _contains_boilerplate(self, text: str) -> bool:
        """检测模板化套话"""
        boilerplate = [
            "该研究具有重要意义",
            "为后续研究提供了方向",
            "值得深入研究",
            "具有广泛应用前景"
        ]
        return any(phrase in text for phrase in boilerplate)
    
    def _stage2_editor_synthesis(self, item: Dict[str, Any], stage1_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Stage 2: 使用 Editor Model 综合多个模型输出"""
        final = {}
        
        final.update(self._vote_structured_fields(stage1_results))
        
        editor_input = self._build_editor_input(item, stage1_results)
        editor_output = self._call_editor_model(editor_input)
        
        if editor_output:
            for field in self.EDITOR_FIELDS:
                final[field] = editor_output.get(field, "")
        else:
            final.update(self._fallback_synthesis(stage1_results))
        
        return final
    
    def _stage2_voting_synthesis(self, stage1_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Stage 2: 使用投票方式综合（备选策略）"""
        final = {}
        
        final.update(self._vote_structured_fields(stage1_results))
        final.update(self._vote_text_fields(stage1_results))
        
        return final
    
    def _vote_structured_fields(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """对结构化字段进行投票"""
        final = {}
        
        for field in self.VOTABLE_FIELDS:
            values = [r.get(field) for r in results if r.get(field) is not None]
            if values:
                if field in ["is_benchmark", "is_open_source_project"]:
                    final[field] = self._vote_boolean(values)
                elif field == "suggested_action":
                    final[field] = self._vote_action(values)
                else:
                    final[field] = self._vote_discrete(values)
        
        return final
    
    def _vote_text_fields(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """对文本字段进行投票（备选方案）"""
        final = {}
        
        for field in self.EDITOR_FIELDS:
            values = [str(r.get(field, "")) for r in results if r.get(field)]
            if values:
                final[field] = self._select_best_text(values, results, field)
        
        return final
    
    def _select_best_text(self, values: List[str], results: List[Dict[str, Any]], field: str) -> str:
        """基于置信度选择最佳文本"""
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
    
    def _vote_discrete(self, values: List[Any]) -> Any:
        """离散值投票"""
        counter = Counter(str(v) for v in values)
        most_common = counter.most_common(1)
        if most_common:
            return most_common[0][0]
        return values[0]
    
    def _vote_boolean(self, values: List[Any]) -> bool:
        """布尔值投票（多数决定）"""
        true_count = sum(1 for v in values if bool(v))
        return true_count > len(values) / 2
    
    def _vote_action(self, values: List[str]) -> str:
        """投票决定行动建议"""
        action_order = {
            "read_pdf": 11,
            "clone_and_run": 10,
            "study_code": 9,
            "use_as_baseline": 8,
            "use_as_eval": 7,
            "skim": 6,
            "watch": 5,
            "read_readme": 4,
            "save": 3,
            "archive": 2,
            "ignore": 1,
        }
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
    
    def _build_editor_input(self, item: Dict[str, Any], stage1_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """构建 Editor Model 的输入"""
        model_outputs = []
        for result in stage1_results:
            model_output = {k: v for k, v in result.items() if k in self.EDITOR_FIELDS}
            model_output.update({
                "model_name": result.get("model_name"),
                "confidence": result.get("confidence"),
                "potential_hallucination_risk": result.get("potential_hallucination_risk")
            })
            model_outputs.append(model_output)
        
        return {
            "item": {
                "title": item.get("title", ""),
                "abstract": item.get("abstract") or item.get("summary", ""),
                "url": item.get("url", ""),
                "source": item.get("source", {}),
                "evidence_text": self._get_evidence_text(item)
            },
            "model_outputs": model_outputs,
            "required_fields": self.EDITOR_FIELDS
        }
    
    def _get_evidence_text(self, item: Dict[str, Any]) -> str:
        """获取用于验证的证据文本"""
        pieces = [
            str(item.get("title", "")),
            str(item.get("abstract") or item.get("summary") or ""),
            json.dumps(item.get("source", {}), ensure_ascii=False),
            str(item.get("url", ""))
        ]
        return "\n".join(piece for piece in pieces if piece.strip())
    
    def _call_editor_model(self, editor_input: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """调用 Editor Model 综合结果"""
        if not self.editor_model:
            return None
        
        api_key = self.editor_model.get("api_key") or ""
        base_url = self.editor_model.get("base_url", "https://api.openai.com/v1").rstrip("/")
        model = self.editor_model.get("model", "gpt-4o-mini")
        
        if not api_key:
            return None

        provider = self.editor_model.get("provider") or self.editor_model.get("type") or "editor"
        client = ChatModelClient(provider=provider, api_key=api_key, base_url=base_url, model=model)
        parsed = client.call_json(
            system_prompt=self._editor_system_prompt(),
            user_payload=editor_input,
            temperature=0.2,
        )
        if parsed and all(key in parsed for key in self.EDITOR_FIELDS):
            return parsed
        log_model_error(provider, model, base_url, "n/a", "Editor response did not include all required summary fields.")
        
        return None
    
    def _editor_system_prompt(self) -> str:
        """Editor Model 的系统提示词"""
        return """你是一位严谨的 AI Research Radar 编辑，负责综合多个 AI 模型的输出。
        
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
"""
    
    def _fallback_synthesis(self, stage1_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Editor Model 失败时的回退策略"""
        final = {}
        
        for field in self.EDITOR_FIELDS:
            values = [str(r.get(field, "")) for r in stage1_results if r.get(field)]
            if values:
                final[field] = self._select_best_text(values, stage1_results, field)
            else:
                final[field] = ""
        
        return final
    
    def rank(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """多模型协作排序"""
        if not self.models:
            return items
        
        all_rankings = []
        for model in self.models:
            try:
                ranking = model.rank(items.copy())
                all_rankings.append((model, ranking))
            except Exception as e:
                print(f"Model {model.name} ranking failed: {e}")
        
        if not all_rankings:
            return items
        
        return self._ensemble_ranking(items, all_rankings)
    
    def _ensemble_ranking(self, items: List[Dict[str, Any]], 
                         rankings: List[tuple[BaseModel, List[Dict[str, Any]]]]) -> List[Dict[str, Any]]:
        """Borda计数综合排序"""
        item_keys = {self._get_item_key(item): item for item in items}
        scores = {key: 0 for key in item_keys}
        
        for model, ranking in rankings:
            weight = model.weight
            for idx, item in enumerate(ranking):
                key = self._get_item_key(item)
                if key in scores:
                    scores[key] += (len(ranking) - idx) * weight
        
        sorted_items = sorted(items, key=lambda x: scores.get(self._get_item_key(x), 0), reverse=True)
        return sorted_items
    
    def _get_item_key(self, item: Dict[str, Any]) -> str:
        """获取条目的唯一标识"""
        return item.get("id") or item.get("url") or item.get("title", "")
    
    @property
    def name(self) -> str:
        """模型名称"""
        return f"Ensemble({', '.join(m.name for m in self.models)})"
