from fastapi import FastAPI, Depends
from utils.utils import get_db
from schemas.game import GameplayInit
from rps_remote_simulator.database.models import Game as GameModel, User as UserModel
from rps_remote_simulator.game import Gameplay
from rps_remote_simulator.errors import DeletedUserWarning, IncorrectPlay
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from datetime import datetime

game = FastAPI()


@game.post("/api/v1/game/play", tags=["games"])
async def create_game(
    choice: str, user_id: int, db: Session = Depends(get_db)
) -> GameModel | None:

    if choice not in Gameplay.OPTIONS:
        raise IncorrectPlay(status_code=400, 
                        detail="{choice} is not a move, stick playing the options!")
    
    db_user = db.get(UserModel, user_id)
    
    if db_user.is_deleted is True:
        raise DeletedUserWarning(status_code=404, detail="User does not exist!")

    new_game = GameplayInit(
        user_id=user_id,
        game_result=Gameplay.play(play=choice),
        date_played=datetime.now(),
    )
    db_game = GameModel(**new_game.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)

    return db_game


@game.get("/api/v1/game/{user_id}/games", tags=["games"])
async def get_user_games(
    user_id: int, offset=0, limit=100, db: Session = Depends(get_db)
) -> List[GameModel] | None:

    db_user = db.get(UserModel, user_id)

    if db_user.is_deleted is True:
        raise DeletedUserWarning(status_code=404, 
        detail="User does not exist! Please register before you can play.")

    return db.scalars(
        select(GameModel)
        .where(GameModel.user_id == user_id)
        .offset(offset)
        .limit(limit)
    ).all()
