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
    :return: User Object
    """
    async with session.begin():
        users_layer = UsersLayer(session)
        user = await users_layer.get_user_by_id(
            user_id=user_id,
        )
        if user is not None:
            return user
