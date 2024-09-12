from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'URL cut service'
    database_url: str
    app_host: str = '127.0.0.1'
    app_port: int = 8080

    class Config:
        env_file = '.env'


settings = Settings()
