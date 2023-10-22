from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (Integer,
                        ForeignKey,
                        String,
                        DateTime,
                        Text,
                        )
from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            relationship
                            )
from datetime import datetime


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    friends = relationship("Friend", cascade="all, delete", primaryjoin="User.id == Friend.friend_id")
    messages = relationship("Message", cascade="all, delete")
    chat_members = relationship("ChatMember", cascade="all, delete", back_populates="user")

class Friend(Base):
    __tablename__ = 'friends'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    friend_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user = relationship("User", primaryjoin="Friend.user_id == User.id", lazy="joined", overlaps="friends")
    friend = relationship("User", primaryjoin="Friend.friend_id == User.id", lazy="joined", overlaps="friends")


class Chat(Base):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    chat_members = relationship("ChatMember", cascade="all, delete", back_populates="chat")
    messages = relationship("Message", cascade="all, delete")

class ChatMember(Base):
    __tablename__ = "chat_members"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    chat_id: Mapped[int] = mapped_column(ForeignKey('chats.id', ondelete="CASCADE"))

    user = relationship("User", back_populates="chat_members")
    chat = relationship("Chat", back_populates="chat_members")


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    chat_id: Mapped[int] = mapped_column(ForeignKey('chats.id', ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
