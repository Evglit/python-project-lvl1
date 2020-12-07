#!/usr/bin/env pyrhon3
"""Greatest common divisor."""

from brain_games import cli

from brain_games.games import gcd


def main():
    """Make a user intreface."""
    name_user = cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    need_answers = 3
    sum_answers = 0
    while sum_answers < need_answers:
        if cli.ask_answer(gcd.what_gcd(), name_user):
            sum_answers += 1
            if sum_answers == need_answers:
                print('Congratulations, {}!'.format(name_user))
        else:
            break


if __name__ == '__main__':
    main()
