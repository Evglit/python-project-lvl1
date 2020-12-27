"""Greatest common divisor for brain-gcd."""

from random import randint
import math


GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_game_data():
    """Returns two numbers and their Greatest Common Divisor."""
    random_number1 = randint(10, 100)
    random_number2 = randint(10, 100)
    game_question = (
        '{} '.format(random_number1)
        +
        '{}'.format(random_number2)
        )
    right_answer = math.gcd(random_number1, random_number2)
    return game_question, str(right_answer)
