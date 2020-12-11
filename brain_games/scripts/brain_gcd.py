#!/usr/bin/env pyrhon3
"""Greatest common divisor."""

from brain_games.games import gcd

from brain_games import engine


def main():
    """Running the brain-gcd."""
    engine.game_engine(gcd.what_gcd, gcd.RULES_GAME)


if __name__ == '__main__':
    main()
