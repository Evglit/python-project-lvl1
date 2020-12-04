#!/usr/bin/env python3
"""Check even."""

from random import randint

import prompt

from brain_games import cli


def is_check_even(name_user):
    """Funtion for check even."""
    need_answers = 3
    sum_answers = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while sum_answers < need_answers:
        number = randint(0, 100)
        print('Question: {}'.format(number))
        if number == 0:
            right_answer = 'no'
        elif number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        player_answer = prompt.string('Your answer: ')
        if player_answer == str(right_answer):
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
    """Make a user interface."""
    is_check_even(cli.welcome_user())


if __name__ == '__main__':
    main()
