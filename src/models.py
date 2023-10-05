from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (MetaData, Integer, ForeignKey,
                        String, DateTime,
                        Text, Float, Boolean
                        )
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


metadata = MetaData()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(50))
