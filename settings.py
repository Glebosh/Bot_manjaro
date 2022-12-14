from pydantic import BaseSettings

class Settings(BaseSettings):

    secret_token: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()
