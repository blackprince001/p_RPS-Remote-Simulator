from pydantic import BaseModel
from datetime import datetime


class GameBase(BaseModel):
    pass


class GameplayInit(GameBase):
    user_id: int
    game_result: dict
    date_played: datetime


class Game(GameBase):
    class Config:
        orm_mode = True
