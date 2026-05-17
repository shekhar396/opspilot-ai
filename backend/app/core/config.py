from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BACKEND_DIR = Path(__file__).resolve().parents[2]
PROJECT_ROOT = BACKEND_DIR.parent


class Settings(BaseSettings):
    app_name: str = "OpsPilot AI"
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    jenkins_url: str | None = None
    jenkins_username: str | None = None
    jenkins_api_token: str | None = None
    jenkins_timeout_seconds: int = 10

    model_config = SettingsConfigDict(
        env_file=(
            PROJECT_ROOT / ".env",
            BACKEND_DIR / ".env",
        ),
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
