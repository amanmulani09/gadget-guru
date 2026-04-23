from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    openai_api_key:str
    environment:str = "development"
    log_level:str = "INFO"
    max_tokens:int = 2000
    temprature:float = 0.3
    rate_limit_per_minute:int = 10
    allowed_origins: list[str] = ["*"]
    
    class Config:
        env_file = ".env"
        
@lru_cache
def get_settings():
    return Settings()