from rps_remote_simulator.game import Gameplay


def test_game_played():
    res = Gameplay.play(play="rock")

    assert res
    assert res['player'] == "rock"


def test_game_failed():
    res = Gameplay.play(play="table")

    assert res
    assert res['player'] is None
    assert res['simulator'] is None