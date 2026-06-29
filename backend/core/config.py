"""config.py
Application settings and configuration loader. Should expose a Settings object with DB_URI, SECRET_KEY, and other env-driven settings.
"""
# core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: "HS256" 
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ENVIRONMENT: str

    class Config:
        env_file = ".env"

settings = Settings()

