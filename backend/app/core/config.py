from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Reads real environment variables first, then the root .env file (when run from backend/)
    model_config = SettingsConfigDict(env_file=("../.env", ".env"), extra="ignore")

    database_url: str
    direct_database_url: str | None = None  # Neon direct connection, used by Alembic
    max_papers_per_workspace: int = 12

    @property
    def alembic_url(self) -> str:
        return self.direct_database_url or self.database_url


settings = Settings()