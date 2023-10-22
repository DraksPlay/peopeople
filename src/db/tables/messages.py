from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from db.layers.messages import MessagesLayer
from models import Message

"""
Module for interacting with the "Message" table
"""

async def get_message_by_id(session: AsyncSession,
                            message_id: int
                            ) -> Optional[Message]:
    """
    Function for getting a user by his ID
    :param session: async session for working with the database
    :param user_id: User ID
    :return: User object
    """
    async with session.begin():
        messages_layer = MessagesLayer(session)
        message = await messages_layer.get_message_by_id(
            message_id=message_id,
        )
        if message is not None:
            return message

async def create_message(session: AsyncSession,
                         text: str,
                         user_id: int,
                         chat_id: int,
                         ) -> Message:
    """
    Function for creating a user
    :param session: async session for working with the database
    :param login: user login
    :param password: user password
    :return: Created user object
    """
    async with session.begin():
        messages_layer = MessagesLayer(session)
        message = await messages_layer.create_message(
            text=text,
            user_id=user_id,
            chat_id=chat_id
        )
        return message

async def update_message(session: AsyncSession,
                         message_id: int,
                         **kwargs
                         ) -> Optional[Message]:
    """
    Function for updating a user
    :param session: async session for working with the database
    :param user_id: User ID
    :param kwargs: dict columns with values
    :return: Updated user object
    """
    async with session.begin():
        messages_layer = MessagesLayer(session)
        message = await messages_layer.update_message(
            message_id=message_id,
            **kwargs
        )
        return message

async def delete_message(session: AsyncSession,
                         message_id: int,
                         ) -> Optional[Message]:
    """
    Function for deleting a user
    :param session: async session for working with the database
    :param user_id: User ID
    :return: Deleted user object
    """
    async with session.begin():
        messages_layer = MessagesLayer(session)
        message = await messages_layer.delete_message(
            message_id=message_id,
        )
        return message
