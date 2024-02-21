from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import User


async def get_user(session: AsyncSession,
                   name: str
                   ) -> Optional[User]:
    async with session.begin():
        query = select(User).where(User.name == name)
        res = await session.execute(query)
        user = res.scalar()
        return user


async def create_user(session: AsyncSession,
                      name: str,
                      ) -> User:
    async with session.begin():
        user = User(
            name=name,
        )
        session.add(user)
        await session.flush()
        await session.refresh(user)
        return user

