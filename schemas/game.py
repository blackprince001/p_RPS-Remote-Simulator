from pydantic import BaseModel


class GameBase(BaseModel):
    pass


class GameplayInit(GameBase):
    user_id: int
    game_result: dict


class Game(GameBase):
    class Config:
        orm_mode = True
