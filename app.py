# Requirements
# It is a CLI-based game, so you need to use the command line to interact with the game. The game should work as follows:
#
# ✅  When the game starts, it should display a welcome message along with the rules of the game.
# ✅ The computer should randomly select a number between 1 and 100.
# ✅ User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess the number.
# The user should be able to enter their guess.
# If the user’s guess is correct, the game should display a congratulatory message along with the number of attempts it took to guess the number.
# If the user’s guess is incorrect, the game should display a message indicating whether the number is greater or less than the user’s guess.
# The game should end when the user guesses the correct number or runs out of chances.

from enum import Enum
from random import randint


class DIFFICULTY_LEVEL(Enum):
    EASY = 10
    MEDIUM = 5
    HARD = 3


def get_random_number() -> int:
    """Returns a random number between 0 and 100"""
    return randint(0, 100)


def grettings() -> None:
    """Print a welcome message along with the rules of the game"""
    print(
        """
        Welcome to the Number Guessing Game!

        I'm thinking of a number between 1 and 100.
        You have 5 chances to guess the correct number.

        Please select the difficulty level:
        1. Easy (10 chances)
        2. Medium (5 chances)
        3. Hard (3 chances)
        """
    )


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


get_difficulty()
