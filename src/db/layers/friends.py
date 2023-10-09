from typing import Optional, Sequence
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models import User, Friend


class FriendsLayer:

    """
    Layer is a class in which queries are being generated
    to work with the Friends table
    """

    def __init__(self,
                 db_session: AsyncSession
                 ) -> None:
        self.db_session = db_session

    async def create_friend(self,
                            user_id: int,
                            friend_id: int,
                            ) -> Friend:
        """
        Function for generating a request to receive a user by his ID
        :param user_id: User ID
        :param friend_id: Friend ID
        :return: Friend object
        """
        friend = Friend(
            user_id=user_id,
            friend_id=friend_id,
        )
        self.db_session.add(friend)
        await self.db_session.flush()
        await self.db_session.refresh(friend)
        return friend

    async def get_friends_by_user_id(self,
                                     user_id: int
                                     ) -> Sequence[Friend]:
        """
        Function for generating a request to get friends by user id
        :param user_id: User ID
        :return: Friends objects
        """
        query = (select(Friend).
                 where(Friend.user_id == user_id)
                 )
        res = await self.db_session.execute(query)
        friends = res.scalars().all()
        return friends
