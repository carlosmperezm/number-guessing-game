# Requirements
# It is a CLI-based game, so you need to use the command line to interact with the game. The game should work as follows:
#
# ✅  When the game starts, it should display a welcome message along with the rules of the game.
# ✅ The computer should randomly select a number between 1 and 100.
# ✅ User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess the number.
# ✅ The user should be able to enter their guess.
# ✅ If the user’s guess is correct, the game should display a congratulatory message along with the number of attempts it took to guess the number.
# ✅ If the user’s guess is incorrect, the game should display a message indicating whether the number is greater or less than the user’s guess.
# ✅ The game should end when the user guesses the correct number or runs out of chances.

from enum import Enum
from random import randint


class DIFFICULTY_LEVEL(Enum):
    EASY = 10
    MEDIUM = 5
    HARD = 3


def get_random_number() -> int:
    """Returns a random number between 0 and 100"""
    return randint(0, 100)


GRETTINGS_MSG: str = """
    Welcome to the Number Guessing Game!

    I'm thinking of a number between 1 and 100.
    You have 5 chances to guess the correct number.

    Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    """


def get_difficulty() -> DIFFICULTY_LEVEL:

    try:
        choice: int = int(input("Enter your choice: "))
        if choice <= 0:
            raise ValueError()
        difficulty_level: DIFFICULTY_LEVEL = list(DIFFICULTY_LEVEL)[choice - 1]
        print(f"Great! You have selected the {difficulty_level.name} difficulty level.")
        return difficulty_level

    except (IndexError, ValueError):
        print("Select a correct difficulty level please.")
        return get_difficulty()


class Game:
    _attemps: int = 5
    _difficulty: DIFFICULTY_LEVEL
    _guess: int = 0
    _number: int = 0

    def __init__(self, greetings_msg: str, random_number: int) -> None:
        print(greetings_msg)
        self._number = random_number

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, new_difficulty: DIFFICULTY_LEVEL) -> None:
        if not isinstance(new_difficulty, DIFFICULTY_LEVEL):
            raise ValueError("Difficulty should be a type DIFFICULTY_LEVEL")
        self._difficulty = new_difficulty
        self._attemps = new_difficulty.value

    def start(self) -> None:
        print("Let's start the game!")
        attemps_counter: int = 0

        while self._guess != self._number:
            print(self._number)

            try:
                self._guess: int = int(input("Enter your guess: "))
                attemps_counter += 1
            except ValueError:
                print("That's not a number")
                continue

            if self._guess > self._number:
                print(f"Incorrect! The number is less than {self._guess}.")
            elif self._guess < self._number:
                print(f"Incorrect! The number is grater  than {self._guess}.")

            if self._attemps == attemps_counter:
                print(
                    "You didn't guess it. You've reached all your attemps. Sorry :( . "
                )
                return

        print(
            f"Congratulations! You guessed the correct number in {attemps_counter} attempts."
        )


if __name__ == "__main__":
    game: Game = Game(GRETTINGS_MSG, get_random_number())
    game.difficulty = get_difficulty()
    game.start()
