from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    sleep_mode: bool = False
    sleep_time: int = 60
    start_sleep_time: int = 00
    telegram_token: str
    telegram_chat_id: str
    olx_urls: list[str]

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
