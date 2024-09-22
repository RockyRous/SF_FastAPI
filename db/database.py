import asyncio

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.future import select

# DATABASE_URL = "postgresql+asyncpg://user:password@localhost/snippet_db"
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/fastapidb"

# Создаем базовый класс для моделей
Base = declarative_base()

# Создаем асинхронный движок SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаем сессионный фабрикатор
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    async with engine.begin() as conn:
        # Создаем все таблицы, определенные в Base.metadata
        await conn.run_sync(Base.metadata.create_all)

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session


async def main():
    await init_db()
    # Здесь можно добавить запуск вашего FastAPI приложения

if __name__ == "__main__":
    asyncio.run(main())