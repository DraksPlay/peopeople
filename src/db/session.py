from typing import Generator
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)
from .tables import Tables


class Database:

    def __init__(self,
                 db_url: str,
                 is_generator: bool = False
                 ) -> None:
        self.db_url = db_url
        self.is_generator = is_generator
        self.tables = Tables

    def get_engine(self):
        engine = create_async_engine(
            self.db_url,
            future=True,
            echo=False,
            execution_options={"isolation_level": "AUTOCOMMIT"},
        )

        return engine

    def get_async_session(self):
        engine = self.get_engine()
        async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
        return async_session

    async def get_session(self) -> AsyncSession:
        async_session = self.get_async_session()
        try:
            async with async_session() as session:
                return session
        finally:
            await session.close()

    def get_session_generator(self):
        async def inner() -> Generator:
            async_session = self.get_async_session()
            try:
                async with async_session() as session:
                    yield session
            finally:
                await session.close()

        return inner

    def __call__(self, *args, **kwargs):
        if self.is_generator:
            return self.get_session_generator()

        return self.get_session()
