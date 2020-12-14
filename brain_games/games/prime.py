"""Prime numbers for brain-prime."""

from random import randint


RULES_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play_game():
    """Returns a number and the answer is simple or not."""
    number = randint(0, 200)
    game_answer = 'Question: {}'.format(number)
    if number > 1:
        i = 2
        while number % i != 0:
            i += 1
        if i == number:
            right_answer = 'yes'
        else:
            right_answer = 'no'
    else:
        right_answer = 'no'
    return game_answer, right_answer
