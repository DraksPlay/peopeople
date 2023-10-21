from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from db.tables import users


router = APIRouter()