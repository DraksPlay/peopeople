from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from db.tables import users
from .schemas import UserUpdateSchema


router = APIRouter()

@router.post("/user")
async def create_user(login: str, password: str, session: AsyncSession = Depends(get_db)):
    user = await users.create_user(session,
                                   login=login,
                                   password=password
                                   )
    return user

@router.get("/user/{user_id}")
async def get_user(user_id: int,
                   session: AsyncSession = Depends(get_db)):
    user = await users.get_user_by_id(session, user_id)
    return user


@router.patch("/user/{user_id}")
async def update_user(user_id: int,
                      user_update_schema: UserUpdateSchema,
                      session: AsyncSession = Depends(get_db)
                      ):
    update_params = dict(filter(lambda x: x[1] is not None, user_update_schema))
    user = await users.update_user(session,
                                   user_id=user_id,
                                   **dict(update_params)
                                   )
    return user

@router.delete("/user/{user_id}")
async def delete_user(user_id: int,
                      session: AsyncSession = Depends(get_db)):
    user = await users.delete_user(session,
                                   user_id=user_id,
                                   )
    return user
