from typing import Optional, Sequence, List
from sqlalchemy import select, update, delete, and_
from sqlalchemy.ext.asyncio import AsyncSession

from models import ChatMember


class ChatMembersLayer:

    """
    Layer is a class in which queries are being generated
    to work with the Friends table
    """

    def __init__(self,
                 db_session: AsyncSession
                 ) -> None:
        self.db_session = db_session

    async def create_chat_member(self,
                                 user_id: int,
                                 chat_id: int,
                                 ) -> ChatMember:
        """
        Function for generating a request to receive a user by his ID
        :param user_id: User ID
        :param friend_id: Friend ID
        :return: Friend object
        """
        chat_member = ChatMember(
            user_id=user_id,
            chat_id=chat_id,
        )
        self.db_session.add(chat_member)
        await self.db_session.flush()
        await self.db_session.refresh(chat_member)
        return chat_member

    async def get_chat_members_by_chat_id(self,
                                          chat_id: int
                                          ) -> Sequence[ChatMember]:
        """
        Function for generating a request to get friends by user id
        :param user_id: User ID
        :return: Friends objects
        """
        query = (select(ChatMember).
                 where(ChatMember.chat_id == chat_id)
                 )
        res = await self.db_session.execute(query)
        chat_members = res.scalars().all()
        return chat_members

    async def delete_chat_member(self,
                                 user_id: int,
                                 chat_id: int
                                 ) -> Optional[ChatMember]:
        """
        Function for generating a request to delete a user by his ID
        :param user_id:
        :return: Deleted user object
        """
        query = (
            delete(ChatMember)
            .where(and_(ChatMember.user_id == user_id, ChatMember.chat_id == chat_id))
            .returning(ChatMember)
        )
        res = await self.db_session.execute(query)
        chat_member = res.fetchone()
        if chat_member is not None:
            return chat_member[0]