#!/usr/bin/env python3
"""Arithmetic progression."""

from brain_games import cli

from brain_games.games import progression


def main():
    """Make a user intreface."""
    name_user = cli.welcome_user()
    print('What number is missing in the progression?')
    need_answers = 3
    sum_answers = 0
    while sum_answers < need_answers:
        if cli.ask_answer(progression.create_progression(), name_user):
            sum_answers += 1
            if sum_answers == need_answers:
                print('Congratulations, {}!'.format(name_user))
        else:
            break


if __name__ == '__main__':
    main()
