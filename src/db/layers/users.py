from typing import Optional
from sqlalchemy import select, update, delete
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

    async def create_user(self,
                          login: str,
                          password: str,
                          ) -> User:
        """
        Function for generating a request to receive a user by his ID
        :param login: User ID
        :param password:
        :return: User object
        """
        user = User(
            login=login,
            password=password,
        )
        self.db_session.add(user)
        await self.db_session.flush()
        await self.db_session.refresh(user)
        return user

    async def get_user_by_id(self,
                             user_id: int
                             ) -> Optional[User]:
        """
        Function for generating a request to receive a user by his ID
        :param user_id: User ID
        :return: User object
        """
        query = select(User).where(User.id == user_id)
        res = await self.db_session.execute(query)
        user = res.scalar()
        return user

    async def update_user(self,
                          user_id,
                          **kwargs
                          ) -> Optional[User]:
        """
        Function for generating a request to update a user by his ID
        :param user_id: User ID
        :param kwargs: dict columns with values
        :return: Updated user Object
        """
        query = (
            update(User)
            .where(User.id == user_id)
            .values(kwargs)
            .returning(User)
        )
        res = await self.db_session.execute(query)
        user = res.fetchone()
        if user is not None:
            return user[0]

    async def delete_user(self,
                          user_id: int
                          ) -> Optional[User]:
        """
        Function for generating a request to delete a user by his ID
        :param user_id:
        :return: Deleted user object
        """
        query = (
            delete(User)
            .where(User.id == user_id)
            .returning(User)
        )
        res = await self.db_session.execute(query)
        user = res.fetchone()
        if user is not None:
            return user[0]
