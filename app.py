from routers.game_end import game
from routers.user_end import user
from routers.admin_end import admin
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World!"}


app.include_router(game.router)
app.include_router(user.router)
app.include_router(admin.router)