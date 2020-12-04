#!/usr/bin/env python3
"""Prime numbers."""

from random import randint

import prompt

from brain_games import cli


def is_prime_numbers(name_user):
    """Funtion for check even."""
    need_answers = 3
    sum_answers = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while sum_answers < need_answers:
        number = randint(0, 200)
        print('Question: {}'.format(number))
        if number > 1:
            i = 2
            while number % i != 0:
                i += 1
            if i == number:
                right_answer = 'yes'
            else:
                right_answer = 'no'
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
    is_prime_numbers(cli.welcome_user())


if __name__ == '__main__':
    main()
