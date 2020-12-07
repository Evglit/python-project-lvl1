"""Check even for brain-even."""

from random import randint


def is_check_even():
    """Prints a number. Returns even or not."""
    number = randint(0, 100)
    print('Question: {}'.format(number))
    if number == 0:
        right_answer = 'no'
    elif number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer
