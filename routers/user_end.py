from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from rps_remote_simulator.database.models import User as UserModel
from rps_remote_simulator.errors import DeletedUserWarning
from utils.utils import get_db

user = FastAPI()


@user.post("/api/v1/user/create", tags=["users"])
async def create_user(
    new_user: UserCreate, db: Session = Depends(get_db)
) -> UserModel | None:
    db_user = UserModel(**new_user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@user.get("/api/v1/user/{user_id}", tags=["users"])
async def get_user(user_id: int, db: Session = Depends(get_db)) -> UserModel | None:
    db_user = db.get(UserModel, user_id)

    if db_user.is_deleted is True:
        raise DeletedUserWarning(status_code=404, detail=
        f"User with {user_id} does not exist!")

    return db_user


@user.patch("/api/v1/user/{user_id}", tags=["users"])
async def change_username(
    user_id: int, new_username: str, db: Session = Depends(get_db)
) -> None:
    db_user = db.get(UserModel, user_id)
    db_user.username = new_username
    db.commit()
    db.refresh(db_user)
