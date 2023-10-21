from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from db.tables import friends


router = APIRouter()

@router.post("/friend")
async def create_friend(user_id: int, friend_id: int,
                        session: AsyncSession = Depends(get_db)):

    friend = await friends.create_friend(session,
                                         user_id=user_id,
                                         friend_id=friend_id
                                         )
    return friend


@router.get("/friend/{user_id}")
async def get_friends(user_id: int,
                      session: AsyncSession = Depends(get_db)):

    friend = await friends.get_friends_by_user_id(session,
                                                  user_id=user_id,
                                                  )
    return friend


@router.delete("/friend")
async def delete_friend(user_id: int,
                        friend_id: int,
                        session: AsyncSession = Depends(get_db)):

    friend = await friends.delete_friend(session,
                                         user_id=user_id,
                                         friend_id=friend_id
                                         )
    return friend
