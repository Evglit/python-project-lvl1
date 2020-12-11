#!/usr/bin/env python3
"""Check even."""

from brain_games.games import even

from brain_games import engine


def main():
    """Running the brain-even."""
    engine.game_engine(even.is_check_even, even.RULES_GAME)


if __name__ == '__main__':
    main()
