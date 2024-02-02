from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import Database
from config import DB_URL
from .schemas import (
    MessageCreateSchema,
)


db = Database(DB_URL, is_generator=True)
router = APIRouter()

@router.get("/messages")
async def get_messages(session: AsyncSession = Depends(db())):
    messages = await db.tables.message.get_messages(session)

    return messages

@router.post("/message")
async def create_message(message_create: MessageCreateSchema,
                         session: AsyncSession = Depends(db())):
    new_message = await db.tables.message.create_message(session, message_create.text)

    return new_message
