import sqlalchemy as sa
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

# 1. Используем асинхронный драйвер aiosqlite
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./db/test_database.sqlite"

# 2. Создаем асинхронный движок
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=False)

# 3. Создаем фабрику асинхронных сессий
async_session = async_sessionmaker(engine, expire_on_commit=False)

# 4. Базовый класс для всех моделей (обязательно с AsyncAttrs)
class Base(AsyncAttrs, DeclarativeBase):
    pass

# 5. Асинхронная функция для создания таблиц (вызывается при старте сервера)
async def init_db():
    async with engine.begin() as conn:
        from data import __all_models
        await conn.run_sync(Base.metadata.create_all)