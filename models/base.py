from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseModel(ABC):
    """所有模型插件的基类接口"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.api_key = config.get("api_key")
        self.base_url = config.get("base_url")
        self.model_name = config.get("model")
        self.weight = config.get("weight", 1.0)
    
    @abstractmethod
    def summarize(self, item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """生成摘要，返回包含 what_is_it, problem, method_or_contribution, 
        why_important, deep_read, suggested_action 的字典"""
        pass
    
    @abstractmethod
    def rank(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """对条目排序/评分，返回排序后的列表"""
        pass
    
    @property
    def name(self) -> str:
        """模型名称"""
        return self.__class__.__name__.replace("Model", "")
    
    def __repr__(self) -> str:
        return f"<{self.name} model={self.model_name}>"
