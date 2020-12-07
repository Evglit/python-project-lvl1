"""Command line interface for brain-games."""

import prompt


def welcome_user():
    """Greets the user and asks for their name. Returns the username."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def ask_answer(right_answer, name_user):
    """Asks for an answer, compares with the correct answer.
    Returns true or false."""
    player_answer = prompt.string('Your answer: ')
    if player_answer == str(right_answer):
        print('Correct!')
        return True
    else:
        print(
            "'{}' is wrong answer ;(. ".format(player_answer)
            +
            "Correct answer was '{}'.".format(right_answer)
            )
        print("Let's try again, {}!".format(name_user))
        return False
