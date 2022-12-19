from fastapi import FastAPI

game = FastAPI()


@game.post("/api/v1/game", tags=["games"])
async def create_game():
    return {}
