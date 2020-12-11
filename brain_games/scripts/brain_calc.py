#!/usr/bin/env python3
"""Calculator."""

from brain_games.games import calc

from brain_games import engine


def main():
    """Running the brain-calc."""
    engine.game_engine(calc.calculator, calc.RULES_GAME)


if __name__ == '__main__':
    main()
