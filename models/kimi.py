from .base import BaseModel
from typing import Any, Dict, List, Optional
import json
import requests


class KimiModel(BaseModel):
    """Kimi API 实现"""
    
    DEFAULT_BASE_URL = "https://api.moonshot.cn/v1"
    DEFAULT_MODEL = "moonshot-v1-8k"
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        if not self.base_url:
            self.base_url = self.DEFAULT_BASE_URL
        if not self.model_name:
            self.model_name = self.DEFAULT_MODEL
    
    def summarize(self, item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if not self.api_key:
            return None
        
        prompt = self._build_prompt(item)
        try:
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
                        {"role": "user", "content": json.dumps(prompt, ensure_ascii=False)}
                    ],
                    "temperature": 0.2,
                    "response_format": {"type": "json_object"},
                    "timeout": 60
                },
                timeout=60
            )
            response.raise_for_status()
            parsed = json.loads(response.json()["choices"][0]["message"]["content"])
            return self._validate_response(parsed)
        except Exception:
            return None
    
    def rank(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return sorted(items, key=lambda x: x.get("scores", {}).get("research_relevance", 0), reverse=True)
    
    def _build_prompt(self, item: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "title": item.get("title"),
            "source": item.get("source", {}),
            "url": item.get("url"),
            "abstract_or_excerpt": item.get("summary", "")[:2000],
            "primary_section": item.get("primary_section", {}),
            "matched_sections": item.get("matched_sections", []),
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
                "suggested_action": "建议行动，只能是 read_pdf / skim / save / reproduce / ignore 之一"
            }
        }
    
    def _system_prompt(self) -> str:
        return (
            "你是严谨的 AI research radar 编辑，面向一位关注长上下文、Agent、开放世界学习和模型压缩的研究者。"
            "用自然、具体、克制的中文写摘要，不营销，不编造，不重复套话。"
            "只基于输入信息；信息不足时直接说明需要打开原文确认。"
            "避免模板化表达，不要按来源类型写泛泛的跟踪价值判断。"
            "返回严格 JSON，字段必须且只能包含："
            "what_is_it, problem, method_or_contribution, why_important, deep_read, suggested_action。"
            "suggested_action 只能是 read_pdf、skim、save、reproduce、ignore 之一。"
            "每个字段 1-2 句，尽量指出具体方法名、任务、数据、系统或实验线索。"
        )
    
    def _validate_response(self, parsed: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        required = {"what_is_it", "problem", "method_or_contribution", 
                   "why_important", "deep_read", "suggested_action"}
        if all(key in parsed for key in required):
            return parsed
        return None
