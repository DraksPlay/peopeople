from fastapi import APIRouter


router = APIRouter()

@router.get("/messages")
async def get_messages():
    ...

@router.post("/message")
async def get_message():
    ...
