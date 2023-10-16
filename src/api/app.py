from fastapi import FastAPI, WebSocket
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import API_URL
from db.session import get_db
from db.tables import users, friends


app = FastAPI(docs_url=API_URL)


@app.post("/user")
async def create_user(session: AsyncSession = Depends(get_db)):
    login = "draksplay"
    password = "admin"
    user = await users.create_user(session,
                                   login=login,
                                   password=password
                                   )
    return user

@app.get("/user")
async def get_user(user_id: int,
                   session: AsyncSession = Depends(get_db)):
    user = await users.get_user_by_id(session, user_id)
    return user


@app.patch("/user")
async def update_user(user_id: int,
                      session: AsyncSession = Depends(get_db),
                      ):
    new_login = "draksplay123"
    user = await users.update_user(session,
                                   user_id=user_id,
                                   login=new_login
                                   )
    return user

@app.delete("/user")
async def delete_user(user_id: int,
                      session: AsyncSession = Depends(get_db)):
    user = await users.delete_user(session,
                                   user_id=user_id,
                                   )
    return user


@app.post("/friend")
async def create_friend(user_id: int, friend_id: int,
                        session: AsyncSession = Depends(get_db)):

    friend = await friends.create_friend(session,
                                         user_id=user_id,
                                         friend_id=friend_id
                                         )
    return friend


@app.get("/friend")
async def get_friends(user_id: int,
                      session: AsyncSession = Depends(get_db)):

    friend = await friends.get_friends_by_user_id(session,
                                   user_id=user_id,
                                   )
    return friend