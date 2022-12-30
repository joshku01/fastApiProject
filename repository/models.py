from sqlalchemy import Boolean, Column, Integer, String
from repository.database import Base
from .database import engine


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)


def create_table():
    Base.metadata.create_all(engine)
