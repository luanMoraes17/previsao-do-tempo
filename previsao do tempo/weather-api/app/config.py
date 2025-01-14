from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENWEATHER_API_KEY: str
    EMAIL_SENDER: str
    EMAIL_PASSWORD: str

    class Config:
        env_file = ".env"

settings = Settings() 