from .summary_model import ProviderSummaryModel


class DeepSeekModel(ProviderSummaryModel):
    """DeepSeek API implementation."""

    PROVIDER = "deepseek"
    DEFAULT_BASE_URL = "https://api.deepseek.com"
    DEFAULT_MODEL = "deepseek-v4-flash"
    RANK_SCORE_KEY = "personal_score"
