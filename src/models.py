from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)
from sqlalchemy import (
    BigInteger,
    String
)

from settings.messanger import MESSAGE_TEXT_MAX_LENGTH


class Base(DeclarativeBase):
    pass


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(MESSAGE_TEXT_MAX_LENGTH))
