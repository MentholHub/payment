from pathlib import Path

from pydantic import AmqpDsn, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path.cwd() / ".env"


class PostrgesSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_prefix="POSTGRES_",
        extra="ignore",
    )

    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    DATABASE: str

    @property
    def url(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql+asyncpg",
                host=self.HOST,
                port=self.PORT,
                username=self.USER,
                password=self.PASSWORD,
                path=self.DATABASE,
            )
        )


class RabbitSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_prefix="RABBITMQ_",
        extra="ignore",
    )

    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    EXCHANGE: str

    @property
    def url(self) -> str:
        return str(
            AmqpDsn.build(
                scheme="amqp",
                host=self.HOST,
                port=self.PORT,
                username=self.USER,
                password=self.PASSWORD,
            )
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        extra="ignore",
    )

    DEBUG: bool
    TOKEN: str

    DATABASE: PostrgesSettings = PostrgesSettings()
    RABBITMQ: RabbitSettings = RabbitSettings()


settings = Settings()
