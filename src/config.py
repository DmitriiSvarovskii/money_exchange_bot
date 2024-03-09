from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PYTHONPATH: str

    BOT_TOKEN: str
    DOMEN_URL: str

    WEBHOOK_SECRET: str
    WEB_SERVER_HOST: str
    WEB_SERVER_PORT: int

    REDIS_HOST: str
    REDIS_PORT: int

    @property
    def WEBHOOK_PATH(self):
        return (f"/bot/{self.BOT_TOKEN}")

    @property
    def WEBHOOK_URL(self):
        return (f"{self.DOMEN_URL}{self.WEBHOOK_PATH}")

    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8')


settings = Settings()
