#!/usr/bin/env pyrhon3
"""Greatest common divisor."""

from random import randint

import prompt

from brain_games import cli


def gcd(name_user):
    """Function for finding the greatest common divisor."""
    need_answers = 3
    sum_answers = 0
    print('Find the greatest common divisor of given numbers.')
    while sum_answers < need_answers:
        number1 = randint(0, 100)
        number2 = randint(0, 100)
        print('Question: {} '.format(number1) + '{}'.format(number2))
        while number1 != 0 and number2 != 0:
            if number1 > number2:
                number1 %= number2
            else:
                number2 %= number1
        right_answer = number1 + number2
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
    gcd(cli.welcome_user())


if __name__ == '__main__':
    main()
