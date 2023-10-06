from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User


class UsersLayer:

    """
    Layer is a class in which queries are being generated
    to work with the Users table
    """

    def __init__(self,
                 db_session: AsyncSession
                 ) -> None:
        self.db_session = db_session

    async def get_user_by_id(self,
                             user_id: int
                             ) -> Optional[User]:
        """
        Function for generating a request to receive a user by his ID
        :param user_id: User ID
        :return: User Object
        """
        query = select(User).where(User.id == user_id)
        res = await self.db_session.execute(query)
        user_row = res.fetchone()
        if user_row is not None:
            return user_row[0]

