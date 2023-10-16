import asyncio
import pytest
from typing import AsyncGenerator, Generator
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from fastapi.testclient import TestClient
from httpx import AsyncClient


import src.config as config
from src.models import Base
from src.api.app import app
from src.db.session import get_db


engine_test = create_async_engine(
    config.DATABASE_URL_TEST,
    future=True,
    execution_options={"isolation_level": "AUTOCOMMIT"},
)

async_session = async_sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)

Base.metadata.bind = engine_test

async def override_get_db() -> Generator:
    """Dependency for getting async session"""
    try:
        async with async_session() as session:
            yield session
    finally:
        await session.close()


app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

# SETUP
@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

client = TestClient(app)

@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac