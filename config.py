import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    cppm_server: str
    client_id: str
    client_secret: str

    class Config:
        env_file = ".env"


settings = Settings()
