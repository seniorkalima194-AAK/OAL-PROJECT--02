"""config.py
Application settings and configuration loader. Should expose a Settings object with DB_URI, SECRET_KEY, and other env-driven settings.
"""
# core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: "HS256" 
    ACCESS_TOKEN_EXPIRE_MINUTES: zint
    ENVIRONMENT: str

    class Config:
        env_file = ".env"

settings = Settings()


from pydantic_settings import BaseSettings
from pydantic import SecretStr

from functools import lru_cache


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    STUDENT_SCORE_THRESHOLD_LOW: float
    STUDENT_SCORE_THRESHOLD_HIGH: float

    MAX_UPLOAD_SIZE_MB: int
    SCORE_VERSION: str
    ENVIRONMENT: str  # "development" | "production"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()