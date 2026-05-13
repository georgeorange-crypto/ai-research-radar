from .summary_model import ProviderSummaryModel


class KimiModel(ProviderSummaryModel):
    """Kimi API implementation."""

    PROVIDER = "kimi"
    DEFAULT_BASE_URL = "https://api.moonshot.cn/v1"
    DEFAULT_MODEL = "moonshot-v1-8k"
    RANK_SCORE_KEY = "research_relevance"
