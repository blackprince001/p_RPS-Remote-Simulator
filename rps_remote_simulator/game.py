from random import choice


class Gameplay:

    OPTIONS = ["rock", "paper", "scissors"]

    @staticmethod()
    def play(self, play: str) -> dict:
        if play not in self.OPTIONS:
            return {"player": None, "simulator": None}

        simulator_choice = choice(self.OPTIONS)

        return {"player": play, "simulator": simulator_choice}
