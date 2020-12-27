"""Engine of brain-games."""


import prompt


CORRECT_ANSWERS_REQUIRED = 3


def launch_game_engine(game):
    """Launch game engine of brain-games."""
    name_user = ask_question(
        'Welcome to the Brain Games!',
        'May I have your name?'
        )
    print('Hello, {}!'.format(name_user))
    print('{}'.format(game.GAME_RULE))
    correct_answers_given = 0
    while correct_answers_given < CORRECT_ANSWERS_REQUIRED:
        game_question, right_answer = game.get_game_data()
        player_answer = ask_question(
            'Question: ' + game_question,
            'Your answer:'
            )
        if player_answer == right_answer:
            print('Correct!')
            correct_answers_given += 1
        else:
            print(
                "'{}' is wrong answer ;(. ".format(player_answer)
                +
                "Correct answer was '{}'.".format(right_answer)
                )
            print("Let's try again, {}!".format(name_user))
            break
    else:
        print('Congratulations, {}!'.format(name_user))


def ask_question(text1, text2):
    """Print text and ask the player. Returns the answer."""
    print('{}'.format(text1))
    answer = prompt.string('{} '.format(text2))
    return answer
