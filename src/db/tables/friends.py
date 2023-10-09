from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from db.layers.friends import FriendsLayer
from models import User, Friend

"""
Module for interacting with the "Friends" table
"""


async def create_friend(session: AsyncSession,
                        user_id: int,
                        friend_id: int,
                        ) -> Friend:
    """
    Function for creating a friend
    :param session: async session for working with the database
    :param user_id: User ID
    :param friend_id: Friend ID
    :return: Created friend object
    """
    async with session.begin():
        friends_layer = FriendsLayer(session)
        friend = await friends_layer.create_friend(
            user_id=user_id,
            friend_id=friend_id
        )
        return friend


async def get_friends_by_user_id(session: AsyncSession,
                                 user_id: int
                                 ) -> Sequence[Friend]:
    """
    Function for getting a friend by his user ID
    :param session: async session for working with the database
    :param user_id: User ID
    :return: Friends of user
    """
    async with session.begin():
        friends_layer = FriendsLayer(session)
        friends = await friends_layer.get_friends_by_user_id(
            user_id=user_id,
        )
        return friends
