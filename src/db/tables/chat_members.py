from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from db.layers.chat_members import ChatMembersLayer
from models import User, ChatMember

"""
Module for interacting with the "Chat Members" table
"""


async def create_chat_member(session: AsyncSession,
                        user_id: int,
                        chat_id: int,
                        ) -> ChatMember:
    """
    Function for creating a friend
    :param session: async session for working with the database
    :param user_id: User ID
    :param friend_id: Friend ID
    :return: Created friend object
    """
    async with session.begin():
        chat_members_layer = ChatMembersLayer(session)
        chat_member = await chat_members_layer.create_chat_member(
            user_id=user_id,
            chat_id=chat_id
        )
        return chat_member


async def get_chat_members_by_chat_id(session: AsyncSession,
                                 chat_id: int
                                 ) -> Sequence[ChatMember]:
    """
    Function for getting a friend by his user ID
    :param session: async session for working with the database
    :param user_id: User ID
    :return: Friends of user
    """
    async with session.begin():
        chat_members_layer = ChatMembersLayer(session)
        chat_member = await chat_members_layer.get_chat_members_by_chat_id(
            chat_id=chat_id,
        )
        return chat_member


async def delete_chat_member(session: AsyncSession,
                             user_id: int,
                             chat_id: int
                             ) -> Optional[ChatMember]:
    """
    Function for deleting a user
    :param session: async session for working with the database
    :param user_id: User ID
    :param chat_id: Chat ID
    :return: Deleted chat member object
    """
    async with session.begin():
        chat_members_layer = ChatMembersLayer(session)
        chat_member = await chat_members_layer.delete_chat_member(
            user_id=user_id,
            chat_id=chat_id
        )
        return chat_member
