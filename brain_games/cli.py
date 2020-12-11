"""Command line interface for brain-games."""

import prompt


def ask_question(text1, text2):
    """Print text and ask the player. Returns the answer."""
    print('{}'.format(text1))
    answer = prompt.string('{} '.format(text2))
    return answer


def welcome_user():
    """Greets the player and asks his name."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
