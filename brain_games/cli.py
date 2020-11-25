"""Command line interface for brain-games."""

import prompt


def welcome_user():
    """Get an user name and promt user."""
    print('Welcome to the Brain Games!\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name