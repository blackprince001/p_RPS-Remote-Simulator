from fastapi import FastAPI

app = FastAPI()


@app.post("/game")
async def create_game():
    return {}
