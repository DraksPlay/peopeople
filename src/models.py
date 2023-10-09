from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (MetaData,
                        Integer,
                        ForeignKey,
                        String,
                        DateTime,
                        Text,
                        Float,
                        Boolean
                        )
from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            relationship
                            )
from datetime import datetime


metadata = MetaData()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    friends = relationship("Friend", cascade="all, delete", primaryjoin="User.id == Friend.friend_id")

class Friend(Base):
    __tablename__ = 'friends'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    friend_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user = relationship("User", primaryjoin="Friend.user_id == User.id", lazy="joined", overlaps="friends")
    friend = relationship("User", primaryjoin="Friend.friend_id == User.id", lazy="joined", overlaps="friends")



