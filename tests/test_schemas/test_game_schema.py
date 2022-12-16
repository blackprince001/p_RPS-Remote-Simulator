from schemas.game import GameplayInit
from rps_remote_simulator.game import Gameplay


def test_game_dataclass():
    played = GameplayInit(
        user_id=1, 
        game_result=Gameplay.play(play="rock")
    )

    assert played.game_result['player'] == "rock"
    assert played.game_result['simulator']