#!/usr/bin/env python3
"""Arithmetic progression."""

from brain_games.games import progression

from brain_games import engine


def main():
    """Running the brain-progession."""
    engine.game_engine(progression.create_progression, progression.RULES_GAME)


if __name__ == '__main__':
    main()
