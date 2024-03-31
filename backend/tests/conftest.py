from typing import AsyncGenerator
import pytest
from httpx import AsyncClient

from db.session import AsyncDatabase
from config import (
    DB_URL
)
from backend.api.app import app
from backend.api.models import Base


db = AsyncDatabase(DB_URL)
engine_test = db.get_aengine()
Base.metadata.bind = engine_test


@pytest.fixture(autouse=True, scope='session')
async def setup_db():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
