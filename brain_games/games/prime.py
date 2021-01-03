"""Prime numbers for brain-prime."""

from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game_data():
    """Returns a number and the answer is simple or not."""
    random_number = randint(0, 200)
    game_question = '{}'.format(random_number)
    right_answer = 'yes' if is_prime(random_number) else 'no'
    return game_question, right_answer


def is_prime(number):
    if number > 1:
        i = 2
        while number % i != 0 and i ** 2 <= number:
            i += 1
        if i ** 2 > number:
            return True
        else:
            return False
    else:
        return False
