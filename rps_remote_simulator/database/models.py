from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    date_created = Column(DateTime, nullable=False)
    