"""Prime numbers for brain-prime."""

from random import randint


def is_prime_numbers():
    """Prints a number. Returns simple or not."""
    number = randint(0, 200)
    print('Question: {}'.format(number))
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
    return right_answer
