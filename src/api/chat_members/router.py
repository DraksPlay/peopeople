from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from db.tables import chat_members


router = APIRouter()


@router.post("/chat_member")
async def create_chat_member(user_id: int,
                             chat_id: int,
                             session: AsyncSession = Depends(get_db)):

    chat_member = await chat_members.create_chat_member(session,
                                                        user_id=user_id,
                                                        chat_id=chat_id
                                                        )
    return chat_member


@router.get("/chat_member/{chat_id}")
async def get_chat_members(chat_id: int,
                           session: AsyncSession = Depends(get_db)):

    chat_member = await chat_members.get_chat_members_by_chat_id(session,
                                                                 chat_id=chat_id,
                                                                 )
    return chat_member


@router.delete("/chat_member")
async def delete_chat_member(user_id: int,
                             chat_id: int,
                             session: AsyncSession = Depends(get_db)):

    chat_member = await chat_members.delete_chat_member(session,
                                                        user_id=user_id,
                                                        chat_id=chat_id
                                                        )
    return chat_member
