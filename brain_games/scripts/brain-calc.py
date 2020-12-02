#!/usr/bin/env python3
"""Calculator."""

from random import randint

import prompt

from brain_games import cli


def calculator(name_user):
    """Funtion for colculator."""
    need_answers = 3
    sum_answers = 0
    print('Welcome to the Brain Games!')
    while sum_answers < need_answers:
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
    """Make a user intreface."""
    calculator(cli.welcome_user())


if __name__ == '__main__':
    main()
