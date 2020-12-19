"""Calculator for brain-calc."""

from random import randint, choice


RULES_GAME = 'What is the result of the expression?'


def play_game():
    """Returns a mathematical expression
    and the correct answer."""
    random_number1 = randint(0, 100)
    random_number2 = randint(0, 100)
    operations = ['+', '-', '*']
    current_operation = choice(operations)
    if current_operation == '+':
        right_answer = random_number1 + random_number2
    if current_operation == '-':
        right_answer = random_number1 - random_number2
    if current_operation == '*':
        right_answer = random_number1 * random_number2
    game_question = (
        'Question: {}'.format(random_number1)
        +
        ' {} '.format(current_operation)
        +
        '{}'.format(random_number2)
        )
    return game_question, str(right_answer)
