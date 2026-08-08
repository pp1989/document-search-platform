from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    app_name: str = Field(alias="APP_NAME")
    app_version: str = Field(alias="APP_VERSION")

    app_env: str = Field(alias="APP_ENV")

    debug: bool = Field(alias="DEBUG")

    host: str = Field(alias="HOST")
    port: int = Field(alias="PORT")

    log_level: str = Field(alias="LOG_LEVEL")

    postgres_host: str = Field(alias="POSTGRES_HOST")
    postgres_port: int = Field(alias="POSTGRES_PORT")
    postgres_db: str = Field(alias="POSTGRES_DB")
    postgres_user: str = Field(alias="POSTGRES_USER")
    postgres_password: str = Field(alias="POSTGRES_PASSWORD")

    ollama_base_url: str = Field(alias="OLLAMA_BASE_URL")
    ollama_model: str = Field(alias="OLLAMA_MODEL")

    phoenix_endpoint: str = Field(alias="PHOENIX_ENDPOINT")

    upload_dir: str = Field(alias="UPLOAD_DIR")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()