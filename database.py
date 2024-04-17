from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from config import DATABASE_URL

engine = create_async_engine(
    # url=DATABASE_URL,
    "sqlite+aiosqlite:///category.db", # Заменить на нормальный URL и нормальную базу
    echo=True,
    )

new_session = async_sessionmaker(engine)
Base = declarative_base()



async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)