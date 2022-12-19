from fastapi import FastAPI

user = FastAPI()


@user.get("/api/v1/users", tags=["users"])
async def get_users():
    return {}
