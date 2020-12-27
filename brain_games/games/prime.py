"""Prime numbers for brain-prime."""

from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game_data():
    """Returns a number and the answer is simple or not."""
    random_number = randint(0, 200)
    game_question = '{}'.format(random_number)
    return game_question, is_prime(random_number)


def is_prime(number):
    if number > 1:
        i = 2
        while number % i != 0 and i <= number / 2:
            i += 1
        if number == i:
            return 'yes'
        else:
            return 'no'
    else:
        return 'no'
