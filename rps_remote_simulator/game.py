from random import choice


class Gameplay:

    OPTIONS = ["rock", "paper", "scissors"]

    @staticmethod
    def play(play: str) -> dict:
        if play not in Gameplay.OPTIONS:
            return {"player": None, "simulator": None}

        simulator_choice = choice(Gameplay.OPTIONS)

        return {"player": play, "simulator": simulator_choice}
