from sqlalchemy import Column, String, DateTime, Integer, JSON, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Game(Base):
    __tablename__ = "games"

    user_id = Column(ForeignKey("user.id"), primary_key=True)
    game_result = Column(JSON, nullable=False)

    user = relationship("User", back_populates="gameplays", lazy="selectin")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    date_created = Column(DateTime, nullable=False)

    is_admin = Column(Boolean, nullable=False, default=True)

    gameplays: list[Game] = relationship(
        "Game", back_populates="user", lazy="selectin"
    )
