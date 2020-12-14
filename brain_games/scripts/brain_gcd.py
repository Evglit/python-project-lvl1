#!/usr/bin/env pyrhon3
"""Greatest common divisor."""

from brain_games.games import gcd

from brain_games import engine


def main():
    """Running the brain-gcd."""
    engine.game_engine(gcd)


if __name__ == '__main__':
    main()
