"""Check even for brain-even."""

from random import randint


RULES_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_game():
    """Returns a number and the answer is even or not."""
    random_number = randint(0, 100)
    game_question = 'Question: {}'.format(random_number)
    if random_number == 0:
        right_answer = 'no'
    right_answer = 'yes' if random_number % 2 == 0 else 'no'
    return game_question, right_answer
