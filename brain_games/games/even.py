"""Check even for brain-even."""

from random import randint


RULES_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_check_even():
    """Returns a number and the answer is even or not."""
    number = randint(0, 100)
    game_question = 'Question: {}'.format(number)
    if number == 0:
        right_answer = 'no'
    elif number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return game_question, right_answer
