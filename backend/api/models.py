from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)
from sqlalchemy import (
    BigInteger,
    String,
    ForeignKey
)

from settings.messanger import (
    MESSAGE_TEXT_MAX_LENGTH,
    USER_NAME_MAX_LENGTH
)


class Base(DeclarativeBase):
    pass


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(MESSAGE_TEXT_MAX_LENGTH))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship("User", back_populates="messages")


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(USER_NAME_MAX_LENGTH))

    messages: Mapped[list["Message"]] = relationship("Message", back_populates="user")
