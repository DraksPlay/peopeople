from typing import Optional
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models import Message


class MessagesLayer:

    """
    Layer is a class in which queries are being generated
    to work with the Users table
    """

    def __init__(self,
                 db_session: AsyncSession
                 ) -> None:
        self.db_session = db_session

    async def create_message(self,
                             text: str,
                             user_id: int,
                             chat_id: int,
                             ) -> Message:
        """
        Function for generating a request to receive a message by his ID
        :param login: User ID
        :param password:
        :return: User object
        """
        message = Message(
            user_id=user_id,
            chat_id=chat_id,
            text=text
        )
        self.db_session.add(message)
        await self.db_session.flush()
        await self.db_session.refresh(message)
        return message

    async def get_message_by_id(self,
                                message_id: int
                                ) -> Optional[Message]:
        """
        Function for generating a request to receive a message by his ID.
        :param message_id: Message ID
        :return: Message object
        """
        query = select(Message).where(Message.id == message_id)
        res = await self.db_session.execute(query)
        message = res.scalar()
        return message

    async def update_message(self,
                             message_id,
                             **kwargs
                             ) -> Optional[Message]:
        """
        Function for generating a request to update a user by his ID
        :param message_id: Message ID
        :param kwargs: dict columns with values
        :return: Updated user Object
        """
        query = (
            update(Message)
            .where(Message.id == message_id)
            .values(kwargs)
            .returning(Message)
        )
        res = await self.db_session.execute(query)
        message = res.fetchone()
        if message is not None:
            return message[0]

    async def delete_message(self,
                             message_id: int
                             ) -> Optional[Message]:
        """
        Function for generating a request to delete a user by his ID
        :param message_id:
        :return: Deleted user object
        """
        query = (
            delete(Message)
            .where(Message.id == message_id)
            .returning(Message)
        )
        res = await self.db_session.execute(query)
        message = res.fetchone()
        if message is not None:
            return message[0]
