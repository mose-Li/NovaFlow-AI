from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    APP_NAME: str = "NovaFlow AI"
    APP_VERSION: str = "0.2.0"

    DATABASE_URL: str = "sqlite:///./database/novaflow.db"

    UPLOAD_DIR: Path = Path("uploads")
    LOG_DIR: Path = Path("logs")

    class Config:
        env_file = ".env"


settings = Settings()

settings.UPLOAD_DIR.mkdir(exist_ok=True)
settings.LOG_DIR.mkdir(exist_ok=True)