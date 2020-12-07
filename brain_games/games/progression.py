"""Arithmetic progression for brain-progression."""

from random import randint


def create_progression():
    """Prints an arithmetic progression. Returns the missing number."""
    number1 = randint(0, 100)
    number2 = randint(0, 10)
    size_progression = randint(5, 10)
    arithmetic_progression = [number1]
    i = 0
    while i < size_progression:
        number1 += number2
        arithmetic_progression.append(number1)
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
    print('Question: ' + str_arithmetic_progression)
    return right_answer
