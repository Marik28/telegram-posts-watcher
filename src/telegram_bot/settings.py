from pydantic import BaseSettings


class Settings(BaseSettings):
    telegram_api_token: str

    database_url: str

    vk_api_url: str = "https://api.vk.com/method/"
    vk_api_token: str
    api_version: float = 5.84


settings = Settings()
