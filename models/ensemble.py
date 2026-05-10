from .base import BaseModel
from typing import Any, Dict, List, Optional
from collections import Counter
import json


class EnsembleModel(BaseModel):
    """多模型协作决策引擎"""
    
    STRATEGIES = ["voting", "weighted", "consensus"]
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.strategy = config.get("strategy", "voting")
        self.models = self._load_models()
    
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
    
    def summarize(self, item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """多模型投票生成摘要"""
        if not self.models:
            return None
        
        results = []
        for model in self.models:
            try:
                result = model.summarize(item)
                if result:
                    results.append((model, result))
            except Exception as e:
                print(f"Model {model.name} failed: {e}")
        
        if not results:
            return None
        
        if self.strategy == "voting":
            return self._vote_summary(results)
        elif self.strategy == "weighted":
            return self._weighted_summary(results)
        elif self.strategy == "consensus":
            return self._consensus_summary(results)
        else:
            return self._vote_summary(results)
    
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
    
    def _vote_summary(self, results: List[tuple[BaseModel, Dict[str, Any]]]) -> Dict[str, Any]:
        """简单多数投票"""
        final = {}
        fields = ["what_is_it", "problem", "method_or_contribution", 
                  "why_important", "deep_read", "suggested_action"]
        
        for field in fields:
            values = [r[1].get(field, "") for r in results if r[1].get(field)]
            if not values:
                final[field] = ""
                continue
            
            if field == "suggested_action":
                final[field] = self._vote_action(values)
            else:
                final[field] = self._vote_text(values)
        
        return final
    
    def _weighted_summary(self, results: List[tuple[BaseModel, Dict[str, Any]]]) -> Dict[str, Any]:
        """加权投票（根据模型权重）"""
        final = {}
        fields = ["what_is_it", "problem", "method_or_contribution", 
                  "why_important", "deep_read", "suggested_action"]
        
        for field in fields:
            weighted_values = []
            for model, result in results:
                value = result.get(field, "")
                if value:
                    weighted_values.extend([value] * int(model.weight * 10))
            
            if not weighted_values:
                final[field] = ""
                continue
            
            if field == "suggested_action":
                final[field] = self._vote_action(weighted_values)
            else:
                final[field] = self._vote_text(weighted_values)
        
        return final
    
    def _consensus_summary(self, results: List[tuple[BaseModel, Dict[str, Any]]]) -> Dict[str, Any]:
        """共识模式 - 所有模型达成一致才采用"""
        final = {}
        fields = ["what_is_it", "problem", "method_or_contribution", 
                  "why_important", "deep_read", "suggested_action"]
        
        for field in fields:
            values = [r[1].get(field, "") for r in results if r[1].get(field)]
            if len(values) < len(self.models):
                final[field] = self._vote_text([r[1].get(field, "") for r in results if r[1].get(field)])
            else:
                unique_values = set(values)
                if len(unique_values) == 1:
                    final[field] = values[0]
                else:
                    final[field] = self._vote_text(values)
        
        return final
    
    def _vote_action(self, values: List[str]) -> str:
        """投票决定行动建议"""
        action_order = {"read_pdf": 5, "reproduce": 4, "skim": 3, "save": 2, "ignore": 1}
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
    
    def _vote_text(self, values: List[str]) -> str:
        """投票决定文本字段"""
        if len(values) == 1:
            return values[0]
        
        counter = Counter(values)
        most_common = counter.most_common(1)
        return most_common[0][0] if most_common else ""
    
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
