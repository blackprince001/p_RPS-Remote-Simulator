from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from schemas.user import AdminCreate
from rps_remote_simulator.database.models import User as UserModel, Game as GameModel
from utils.utils import get_db

admin = FastAPI()


@admin.get("/api/v1/admin/users", tags=["admins"])
async def get_users(db: Session = Depends(get_db)) -> List[UserModel] | None:
    return db.scalars(select(UserModel).where(UserModel.is_deleted == False)).all()


@admin.get("/api/v1/admin/users/deleted", tags=["admins"])
async def get_deleted_users(db: Session = Depends(get_db)) -> List[UserModel] | None:
    return db.scalars(select(UserModel).where(UserModel.is_deleted == True)).all()


@admin.get("/api/v1/admin/user/{user_id}", tags=["admins"])
async def get_user(user_id: int, db: Session = Depends(get_db)) -> UserModel | None:
    db_user = db.get(UserModel, user_id)

    if db_user.is_deleted is True:
        # handle this exception well too
        raise Exception("User not found!")

    return db_user


@admin.patch("/api/v1/admin/user/{user_id}", tags=["admins"])
async def delete_user(user_id: int, db: Session = Depends(get_db)) -> None:
    db_user = db.get(UserModel, user_id)

    if db_user.is_deleted is True:
        # change this exception and handle it well with HTTPExceptions
        raise Exception("This user account has already been deleted!")
    db_user.is_deleted = True
    db.commit()
    db.refresh(db_user)


@admin.post("/api/v1/admin/create", tags=["admins"])
async def create_admin(
    new_admin: AdminCreate, db: Session = Depends(get_db)
) -> UserModel | None:
    db_admin = UserModel(**new_admin.dict())
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


@admin.get("/api/v1/admin/{admin_id}", tags=["admins"])
async def get_admin(admin_id: int, db: Session = Depends(get_db)) -> UserModel | None:
    db_admin = db.get(UserModel, admin_id)

    if db_admin.is_admin is False:
        raise Exception("Admin not found!")

    return db_admin


@admin.get("/api/v1/admins", tags=["admins"])
async def get_admins(db: Session = Depends(get_db)) -> List[UserModel] | None:
    return db.scalars(select(UserModel).where(UserModel.is_admin == True)).all()


@admin.get("/api/v1/admins/deleted", tags=["admins"])
async def get_deleted_admins(db: Session = Depends(get_db)) -> List[UserModel] | None:
    return db.scalars(
        select(UserModel)
        .where(UserModel.is_admin == True)
        .where(UserModel.is_deleted == True)
    ).all()


@admin.get("/api/v1/admin/allgames", tags=["admins"])
async def get_all_games(
    offset=0, limit=50, db: Session = Depends(get_db)
) -> List[GameModel] | None:
    return db.scalars(select(GameModel).offset(offset).limit(limit)).all()
