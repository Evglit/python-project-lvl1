"""Command line interface for brain-games."""

import prompt


def welcome_user():
    """Greets the player and asks his name."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
