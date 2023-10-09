from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from db.layers.users import UsersLayer
from models import User

"""
Module for interacting with the "Users" table
"""

async def get_user_by_id(session: AsyncSession,
                         user_id: int
                         ) -> Optional[User]:
    """
    Function for getting a user by his ID
    :param session: async session for working with the database
    :param user_id: User ID
    :return: User object
    """
    async with session.begin():
        users_layer = UsersLayer(session)
        user = await users_layer.get_user_by_id(
            user_id=user_id,
        )
        if user is not None:
            return user

async def create_user(session: AsyncSession,
                      login: str,
                      password: str,
                      ) -> User:
    """
    Function for creating a user
    :param session: async session for working with the database
    :param login: user login
    :param password: user password
    :return: Created user object
    """
    async with session.begin():
        users_layer = UsersLayer(session)
        user = await users_layer.create_user(
            login=login,
            password=password
        )
        return user

async def update_user(session: AsyncSession,
                      user_id: int,
                      **kwargs
                      ) -> Optional[User]:
    """
    Function for updating a user
    :param session: async session for working with the database
    :param user_id: User ID
    :param kwargs: dict columns with values
    :return: Updated user object
    """
    async with session.begin():
        users_layer = UsersLayer(session)
        user = await users_layer.update_user(
            user_id=user_id,
            **kwargs
        )
        return user

async def delete_user(session: AsyncSession,
                      user_id: int,
                      ) -> Optional[User]:
    """
    Function for deleting a user
    :param session: async session for working with the database
    :param user_id: User ID
    :return: Deleted user object
    """
    async with session.begin():
        users_layer = UsersLayer(session)
        user = await users_layer.delete_user(
            user_id=user_id,
        )
        return user
