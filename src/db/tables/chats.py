from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from db.layers.chats import ChatsLayer
from models import Chat

"""
Module for interacting with the "Chats" table
"""


async def create_chat(session: AsyncSession,
                      ) -> Chat:
    """
    Function for creating a chat
    :param session: async session for working with the database
    :return: Created chat object
    """
    async with session.begin():
        chats_layer = ChatsLayer(session)
        chat = await chats_layer.create_chat()
        return chat


async def get_chat_by_id(session: AsyncSession,
                         chat_id: int
                         ) -> Optional[Chat]:
    """
    Function for getting a chat by his ID
    :param session: async session for working with the database
    :param chat_id: Chat ID
    :return: Chat object
    """
    async with session.begin():
        chats_layer = ChatsLayer(session)
        chat = await chats_layer.get_chat_by_id(chat_id=chat_id)
        return chat


async def delete_chat(session: AsyncSession,
                      chat_id: int
                      ) -> Optional[Chat]:
    """
    Function for deleting a chat
    :param session: async session for working with the database
    :param chat_id: Chat ID
    :return: Deleted chat object
    """
    async with session.begin():
        chats_layer = ChatsLayer(session)
        chat = await chats_layer.delete_chat(chat_id=chat_id)
        return chat
