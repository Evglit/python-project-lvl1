"""Prime numbers for brain-prime."""

from random import randint


RULES_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play_game():
    """Returns a number and the answer is simple or not."""
    random_number = randint(0, 200)
    game_question = 'Question: {}'.format(random_number)
    if random_number > 1:
        i = 2
        while random_number % i != 0 and i <= random_number / 2:
            i += 1
        right_answer = 'yes' if random_number == i else 'no'
    else:
        right_answer = 'no'
    return game_question, right_answer
