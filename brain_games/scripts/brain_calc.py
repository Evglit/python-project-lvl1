#!/usr/bin/env python3
"""Calculator."""

from brain_games import cli

from brain_games.games import calc


def main():
    """Make a user intreface."""
    name_user = cli.welcome_user()
    print('What is the result of the expression?')
    need_answers = 3
    sum_answers = 0
    while sum_answers < need_answers:
        if cli.ask_answer(calc.calculator(), name_user):
            sum_answers += 1
            if sum_answers == need_answers:
                print('Congratulations, {}!'.format(name_user))
        else:
            break


if __name__ == '__main__':
    main()
