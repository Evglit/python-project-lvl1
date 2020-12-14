"""Calculator for brain-calc."""

from random import randint


RULES_GAME = 'What is the result of the expression?'


def play_game():
    """Returns a mathematical expression
    and the correct answer."""
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
    game_question = (
        'Question: {}'.format(number1)
        +
        ' {} '.format(oper_str)
        +
        '{}'.format(number2)
        )
    return game_question, right_answer
