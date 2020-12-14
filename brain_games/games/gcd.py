"""Greatest common divisor for brain-gcd."""

from random import randint


RULES_GAME = 'Find the greatest common divisor of given numbers.'


def play_game():
    """Returns two numbers and their Greatest Common Divisor."""
    number1 = randint(10, 100)
    number2 = randint(10, 100)
    game_question = 'Question: {} '.format(number1) + '{}'.format(number2)
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1
    right_answer = number1 + number2
    return game_question, right_answer
