from fastapi import FastAPI, Depends
from utils.utils import get_db
from schemas.game import GameplayInit
from rps_remote_simulator.database.models import Game as GameModel
from rps_remote_simulator.game import Gameplay
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List

game = FastAPI()


@game.post("/api/v1/games", tags=["games"])
async def create_game(
    choice: str, user_id: int, db: Session = Depends(get_db)
) -> GameModel | None:
    # you can handle the choice if it is correct
    # before you continue with the game schema
    # same goes with the user_id
    new_game = GameplayInit(user_id, Gameplay.play(play=choice))
    db_game = GameModel(**new_game.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)

    return db_game


@game.get("/api/v1/game/{user_id}/games", tags=["games"])
async def get_user_games(
    user_id: int, db: Session = Depends(get_db)
) -> List[GameModel] | None:
    # remember to check if the user is not deleted or a game is deleted
    return db.scalars(select(GameModel).where(GameModel.user_id == user_id)).all()
