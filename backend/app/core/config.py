from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    environment: str = Field(default="development")
    demo_mode: bool = Field(default=True)
    api_v1_prefix: str = Field(default="/api/v1")
    frontend_origins: List[str] = Field(default_factory=lambda: ["http://localhost:5173"])
    database_url: str = Field(default="sqlite:///./careerwallah.db")
    sarvam_api_key: str | None = Field(default=None)
    sarvam_chat_model: str = Field(default="bulbul:v1")
    sarvam_api_base: str | None = Field(default=None)

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
