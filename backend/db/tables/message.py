from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import Message


async def get_messages(session: AsyncSession,
                       ) -> Sequence[Message]:
    async with session.begin():
        query = select(Message)
        res = await session.execute(query)
        messages = res.scalars().all()
        return messages


async def create_message(session: AsyncSession,
                         text: str,
                         user_id: int
                         ) -> Message:
    async with session.begin():
        message = Message(
            text=text,
            user_id=user_id
        )
        session.add(message)
        await session.flush()
        await session.refresh(message)
        return message

