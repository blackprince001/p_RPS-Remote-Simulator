from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    username: str
    date_created: datetime
    is_deleted: bool = False


class User(UserBase):
    class Config:
        orm_mode = True


class AdminCreate(UserCreate):
    is_admin: bool = True


class Admin(UserBase):
    class Config:
        orm_mode = True
