"""Arithmetic progression for brain-progression."""

from random import randint


RULES_GAME = 'What number is missing in the progression?'


def play_game():
    """Returns an arithmetic progression and the missing number."""
    random_number = randint(0, 100)
    difference_progression = randint(1, 10)
    size_progression = randint(5, 10)
    arithmetic_progression = [random_number]
    i = 0
    while i < size_progression:
        random_number += difference_progression
        arithmetic_progression.append(random_number)
        i += 1
    hidden_element = randint(0, size_progression - 1)
    right_answer = arithmetic_progression[hidden_element]
    arithmetic_progression[hidden_element] = '..'
    game_question = 'Question: ' + ' '.join(str(x) for x in arithmetic_progression)
    return game_question, str(right_answer)
