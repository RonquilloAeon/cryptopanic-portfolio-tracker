from pydantic import BaseSettings


class Config(BaseSettings):
    API_BASE_URL: str = "https://cryptopanic.com/api/v1/"
    API_TOKEN: str
    LOG_LEVEL: str = "info"

    class Config:
        env_file = ".env"
