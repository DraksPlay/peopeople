from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from db.tables import messages
from .schemas import MessageUpdateSchema


router = APIRouter()

@router.post("/message")
async def create_message(text: str,
                         user_id: int,
                         chat_id: int,
                         session: AsyncSession = Depends(get_db)):
    message = await messages.create_message(session,
                                            text=text,
                                            user_id=user_id,
                                            chat_id=chat_id
                                            )
    return message

@router.get("/message/{message_id}")
async def get_message(message_id: int,
                      session: AsyncSession = Depends(get_db)):
    message = await messages.get_message_by_id(session,
                                               message_id)
    return message


@router.patch("/message/{message_id}")
async def update_message(message_id: int,
                         message_update_schema: MessageUpdateSchema,
                         session: AsyncSession = Depends(get_db)
                         ):
    update_params = dict(filter(lambda x: x[1] is not None, message_update_schema))
    message = await messages.update_message(session,
                                            message_id=message_id,
                                            **dict(update_params)
                                            )
    return message

@router.delete("/message/{message_id}")
async def delete_message(message_id: int,
                         session: AsyncSession = Depends(get_db)):
    message = await messages.delete_message(session,
                                            message_id=message_id,
                                            )
    return message
