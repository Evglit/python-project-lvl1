#!/usr/bin/env python3
"""Arithmetic progression."""

from random import randint

import prompt

from brain_games import cli


def ar_progression(name_user):
    """Function for finding the greatest common divisor."""
    need_answers = 3
    sum_answers = 0
    print('What number is missing in the progression?')
    while sum_answers < need_answers:
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
        player_answer = prompt.string('Your answer: ')
        if int(player_answer) == right_answer:
            sum_answers += 1
            print('Correct!')
            if sum_answers == need_answers:
                print('Congratulations, {}!'.format(name_user))
        else:
            print(
                "'{}' is wrong answer ;(. ".format(player_answer)
                +
                "Correct answer was '{}'.".format(right_answer)
                )
            print("Let's try again, {}!".format(name_user))
            break


def main():
    ar_progression(cli.welcome_user())


if __name__ == '__main__':
    main()
