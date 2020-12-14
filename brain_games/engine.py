"""Engine of brain-games."""


from brain_games import cli


NEED_RIGHT_ANSWERS = 3
GREETING = 'Welcome to the Brain Games!'


def game_engine(game, rules_game):
    """Game engine of brain-games."""
    name_user = cli.ask_question(GREETING, 'May I have your name?')
    print('Hello, {}!'.format(name_user))
    print('{}'.format(rules_game))
    sum_right_answers = 0
    while sum_right_answers < NEED_RIGHT_ANSWERS:
        game_question, right_answer = game()
        player_answer = cli.ask_question(game_question, 'Your answer:')
        if player_answer == str(right_answer):
            print('Correct!')
            sum_right_answers += 1
            if sum_right_answers == NEED_RIGHT_ANSWERS:
                print('Congratulations, {}!'.format(name_user))
        else:
            print(
                "'{}' is wrong answer ;(. ".format(player_answer)
                +
                "Correct answer was '{}'.".format(right_answer)
                )
            print("Let's try again, {}!".format(name_user))
            break
