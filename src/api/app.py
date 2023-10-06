from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import API_URL
from db.session import get_db
from db.tables import users


app = FastAPI(docs_url=API_URL)


@app.get("/user")
async def get_user(db: AsyncSession = Depends(get_db), user_id: int = 0):
    user = await users.get_user_by_id(db, user_id)
    return user
