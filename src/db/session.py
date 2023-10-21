from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

import src.config as config


engine = create_async_engine(
    config.DATABASE_URL,
    future=True,
    echo=False,
    execution_options={"isolation_level": "AUTOCOMMIT"},
)

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> Generator:
    """Dependency for getting async session"""
    try:
        async with async_session() as session:
            yield session
    finally:
        await session.close()
