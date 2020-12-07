"""Calculator for brain-calc."""

from random import randint


def calculator():
    """Prints an expression. Returns the correct answer."""
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    operation = randint(0, 2)
    if operation == 0:
        right_answer = number1 + number2
        oper_str = '+'
    if operation == 1:
        right_answer = number1 - number2
        oper_str = '-'
    if operation == 2:
        right_answer = number1 * number2
        oper_str = '*'
    print(
        'Question: {}'.format(number1) +
        ' {} '.format(oper_str)
        +
        '{}'.format(number2)
        )
    return right_answer
