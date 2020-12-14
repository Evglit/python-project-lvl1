#!/usr/bin/env python3
"""Prime numbers."""

from brain_games.games import prime

from brain_games import engine


def main():
    """Running the brain-prime."""
    engine.game_engine(prime)


if __name__ == '__main__':
    main()
