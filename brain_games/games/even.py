"""Check even for brain-even."""

from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
    """Returns a number and the answer is even or not."""
    random_number = randint(0, 100)
    game_question = '{}'.format(random_number)
    if random_number == 0:
        right_answer = 'no'
    right_answer = 'yes' if random_number % 2 == 0 else 'no'
    return game_question, right_answer
