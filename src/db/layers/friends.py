from typing import Optional, Sequence, List
from sqlalchemy import select, update, delete, and_
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

    async def delete_friend(self,
                            user_id: int,
                            friend_id: int
                            ) -> Optional[Friend]:
        """
        Function for generating a request to delete a user by his ID
        :param user_id:
        :return: Deleted user object
        """
        query = (
            delete(Friend)
            .where(and_(Friend.user_id == user_id, Friend.friend_id == friend_id))
            .returning(Friend)
        )
        res = await self.db_session.execute(query)
        friend = res.fetchone()
        if friend is not None:
            return friend[0]