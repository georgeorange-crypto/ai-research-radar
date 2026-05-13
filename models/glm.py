from .summary_model import ProviderSummaryModel


class GLMModel(ProviderSummaryModel):
    """GLM API implementation."""

    PROVIDER = "glm"
    DEFAULT_BASE_URL = "https://open.bigmodel.cn/api/paas/v4"
    DEFAULT_MODEL = "glm-4.7-flash"
    RANK_SCORE_KEY = "actionability"
