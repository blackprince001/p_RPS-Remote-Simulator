from fastapi import FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from schemas.user import UserCreate
from rps_remote_simulator.database.models import User as UserModel

user = FastAPI()


@user.get("/api/v1/users", tags=["users"])
async def get_users(db: Session) -> List[UserModel, ...] | None:
    return db.scalars(select(UserModel).where(UserModel.is_deleted is False)).all()


@user.get("/api/v1/user/{user_id}", tags=["users"])
async def get_user(db: Session, user_id: int) -> UserModel | None:
    db_user = db.get(UserModel, user_id)

    if db_user.is_deleted is True:
        return db_user

    # handle this exception well too
    raise Exception("User not found!")


@user.post("/api/v1/users", tags=["users"])
async def create_user(db: Session, new_user: UserCreate) -> UserModel | None:
    db_user = UserModel(**new_user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@user.delete("/api/v1/user/{user_id}", tags=["users"])
async def delete_user(db: Session, user_id: int) -> None:
    db_user = get_user(db, user_id)

    if db_user.is_deleted is True:
        # change this exception and handle it well with HTTPExceptions
        raise Exception("This user account has already been deleted!")
