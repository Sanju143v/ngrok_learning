from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str | None = None
    POSTGRES_URL: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    @computed_field  # type: ignore[prop-decorator]
    @property
    def database_uri(self) -> str:
        uri = self.DATABASE_URL or self.POSTGRES_URL
        if not uri:
            raise ValueError("Set DATABASE_URL or POSTGRES_URL in environment variables")

        # Many providers return postgres://, while SQLAlchemy expects postgresql://
        if uri.startswith("postgres://"):
            uri = uri.replace("postgres://", "postgresql://", 1)

        return uri


settings = Settings()
