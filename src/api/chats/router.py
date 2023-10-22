from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from db.tables import chats


router = APIRouter()


@router.post("/chat")
async def create_chat(session: AsyncSession = Depends(get_db)):
    chat = await chats.create_chat(session)
    return chat

@router.get("/chat/{chat_id}")
async def get_chat(chat_id: int,
                   session: AsyncSession = Depends(get_db)):
    chat = await chats.get_chat_by_id(session, chat_id)
    return chat


@router.delete("/chat/{chat_id}")
async def delete_chat(chat_id: int,
                      session: AsyncSession = Depends(get_db)):
    chat = await chats.delete_chat(session,
                                   chat_id=chat_id,
                                   )
    return chat
