from pydantic import BaseSettings

class Settings(BaseSettings):
    app_env: str
    database_url: str
    
    class config:
        env_file = ".env"

settings = Settings()