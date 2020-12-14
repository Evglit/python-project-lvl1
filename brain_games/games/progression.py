"""Arithmetic progression for brain-progression."""

from random import randint


RULES_GAME = 'What number is missing in the progression?'


def play_game():
    """Returns an arithmetic progression and the missing number."""
    number = randint(0, 100)
    difference_progression = randint(1, 10)
    size_progression = randint(5, 10)
    arithmetic_progression = [number]
    i = 0
    while i < size_progression:
        number += difference_progression
        arithmetic_progression.append(number)
        i += 1
    hidden_element = randint(0, size_progression - 1)
    str_arithmetic_progression = ''
    j = 0
    while j < size_progression:
        if str_arithmetic_progression:
            str_arithmetic_progression += ' '
        if j == hidden_element:
            right_answer = arithmetic_progression[j]
            str_arithmetic_progression += '..'
            j += 1
        else:
            str_arithmetic_progression += str(arithmetic_progression[j])
            j += 1
    game_question = 'Question: ' + str_arithmetic_progression
    return game_question, right_answer
