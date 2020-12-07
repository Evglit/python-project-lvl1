"""Greatest common divisor for brain-gcd."""

from random import randint


def what_gcd():
    """Prints two numbers. Returns the Greatest Common Divisor."""
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    print('Question: {} '.format(number1) + '{}'.format(number2))
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1
    right_answer = number1 + number2
    return right_answer
