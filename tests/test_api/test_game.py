from routers.game_end import game as gamesplayed
from fastapi.testclient import TestClient

client = TestClient(gamesplayed)


def test_create_game_success():
    # this is only going to be used to test if a user is already available
    # checks user existence already included in `routers.game_end.create_user`
    arbitrary_id = 1
    choice = "rock"

    new_game_payload = {"user_id": arbitrary_id, "choice": choice}
    game_create_response = client.post(url="/api/v1/game/play", json=new_game_payload)

    assert game_create_response.status_code == 200


def test_create_game_failure():
    # this is only going to be used to test if a user is already available
    # checks user existence already included in `routers.game_end.create_user`
    arbitrary_id = 1000
    choice = "rock"

    new_game_payload = {"user_id": arbitrary_id, "choice": choice}
    game_create_response = client.post(url="/api/v1/game/play", json=new_game_payload)

    assert game_create_response.status_code != 200
    print(game_create_response.status_code)
