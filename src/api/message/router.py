from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import Database
from config import DB_URL

db = Database(DB_URL, is_generator=True)
router = APIRouter()

@router.get("/messages")
async def get_messages(session: AsyncSession = Depends(db())):
    print(session)

@router.post("/message")
async def get_message():
    ...
