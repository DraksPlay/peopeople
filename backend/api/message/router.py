from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db import AsyncDatabase
from config import DB_URL
from .schemas import (
    MessageCreateSchema,
)


router = APIRouter()
db = AsyncDatabase(DB_URL, is_generator=True)

@router.get("/messages")
async def get_messages(session: AsyncSession = Depends(db())):
    messages = await db.tables.message.get_messages(session)

    return messages

@router.post("/message")
async def create_message(message_create: MessageCreateSchema,
                         session: AsyncSession = Depends(db())):
    user = await db.tables.user.get_user(session, message_create.username)
    if user is None:
        user = await db.tables.user.create_user(session, message_create.username)

    new_message = await db.tables.message.create_message(session, message_create.text, user.id)

    return new_message
