from loguru import logger
from config.settings import settings

logger.add(
    settings.LOG_DIR / "novaflow.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
    encoding="utf-8",
)

app_logger = logger