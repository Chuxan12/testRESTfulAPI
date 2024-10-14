import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import MultiHostUrl
from pydantic import PostgresDsn
from pydantic.networks import HttpUrl
import logging

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    
    REDIS_URL: str
    REDIS_PORT: int
    
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    def SQLALCHEMY_DATABASE_URL(self, async_driver: bool = True) -> PostgresDsn:
        #print(self.POSTGRES_USER, self.POSTGRES_PASSWORD, self.POSTGRES_HOST, self.POSTGRES_PORT, self.POSTGRES_DB)
        return MultiHostUrl.build(
        scheme='postgresql+asyncpg' if async_driver else 'postgresql+psycopg2',
        username='test',
        password='password',
        host='db',
        port=5432,
        path='test',
    ).unicode_string()
    
    class Config:
        env_file = '.env'


settings = Settings()