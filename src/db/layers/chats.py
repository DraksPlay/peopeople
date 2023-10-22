from typing import Optional
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models import Chat


class ChatsLayer:

    """
    Layer is a class in which queries are being generated
    to work with the Friends table.
    """

    def __init__(self,
                 db_session: AsyncSession
                 ) -> None:
        self.db_session = db_session

    async def create_chat(self) -> Chat:
        """
        Function for generating a request to receive a chat.
        :return: Chat object
        """
        chat = Chat()
        self.db_session.add(chat)
        await self.db_session.flush()
        await self.db_session.refresh(chat)
        return chat

    async def get_chat_by_id(self,
                             chat_id: int
                             ) -> Optional[Chat]:
        """
        Function for generating a request to get friends by user id.
        :param chat_id: Chat ID
        :return: Chat object
        """
        query = (select(Chat).
                 where(Chat.id == chat_id)
                 )
        res = await self.db_session.execute(query)
        chat = res.scalar()
        return chat

    async def delete_chat(self,
                          chat_id: int,
                          ) -> Optional[Chat]:
        """
        Function for generating a request to delete a user by his ID
        :param chat_id:
        :return: Deleted chat object
        """
        query = (
            delete(Chat)
            .where(Chat.id == chat_id)
            .returning(Chat)
        )
        res = await self.db_session.execute(query)
        chat = res.fetchone()
        if chat is not None:
            return chat[0]
