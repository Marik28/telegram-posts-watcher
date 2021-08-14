import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime, Text,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)


class WallPost(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.utcnow(), nullable=False)
    text = Column(Text, nullable=False)

    def __repr__(self):
        return f"tables.WallPost(id={self.id}, date={self.date}, text={self.text})"
