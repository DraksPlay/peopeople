from typing import (
    Generator,
    Coroutine,
    Any
)
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker
)


from .tables import Tables


class AsyncDatabase:

    def __init__(self,
                 db_url: str,
                 is_generator: bool = False
                 ) -> None:
        self.db_url = db_url
        self.is_generator = is_generator
        self.tables = Tables

    def get_engine(self) -> AsyncEngine:
        engine = create_async_engine(
            self.db_url,
            future=True,
            echo=False,
            execution_options={"isolation_level": "AUTOCOMMIT"},
        )

        return engine

    def get_async_sessionmaker(self) -> async_sessionmaker:
        engine = self.get_engine()
        async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

        return async_session

    async def get_session(self) -> AsyncSession:
        sessionmaker = self.get_async_sessionmaker()
        try:
            async with sessionmaker() as session:
                return session
        finally:
            await session.close()

    def get_session_generator(self) -> "() -> Generator":
        async def inner() -> Generator:
            sessionmaker = self.get_async_sessionmaker()
            try:
                async with sessionmaker() as session:
                    yield session
            finally:
                await session.close()

        return inner

    def __call__(self,
                 *args,
                 **kwargs
                 ) -> "Generator | Coroutine[Any, Any, AsyncSession] | Any":
        if self.is_generator:
            return self.get_session_generator()

        return self.get_session()
