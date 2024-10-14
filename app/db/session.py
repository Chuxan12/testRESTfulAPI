from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from app.core.config import settings
from app.models.base import Base

#DATABASE_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}/{settings.POSTGRES_DB}"

# Создание асинхронного двигателя
engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URL(async_driver=True),
    pool_size=10,  # максимальное количество постоянных соединений
    max_overflow=20,  # дополнительные соединения сверх pool_size
    pool_timeout=30,  # таймаут ожидания соединения
    pool_recycle=1800,  # время перезагрузки соединений
    echo=True  # логирование sql query
)

# Создание фабрики сессий
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False
)

async def get_async_session():
    async with AsyncSessionLocal() as db:
        try:
            yield db
            await db.commit()
        except Exception as e:
            await db.rollback()
            raise e