import asyncio
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from alembic import context
from app.models.base import Base  # Импортируйте ваш базовый класс
from app.core.config import settings  # Импортируйте настройки
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app.db.session import get_async_session  # Импортируйте вашу сессию

# Получаем доступ к объекту конфигурации
config = context.config

# Это необходимо для логирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Импортируйте ваши модели, чтобы Alembic мог их обнаружить
target_metadata = Base.metadata

# Настройка URL базы данных
config.set_main_option('sqlalchemy.url',
                       settings.SQLALCHEMY_DATABASE_URL(async_driver=False))


def run_migrations_online() -> None:
    
    """Run migrations in 'online' mode with sync engine."""

    # Используем синхронный движок для миграций
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    
    with context.begin_transaction():
        context.run_migrations()

def run_migrations():
    if context.is_offline_mode():
        asyncio.run(run_migrations_offline())
    else:
        asyncio.run(run_migrations_online())

if __name__ == "__main__":
    run_migrations()