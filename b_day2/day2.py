import os
from math import prod
from pathlib import Path


def part_one(games: list[str]) -> int:
    """
    Looks through the games played and ensures that none of the cubes of a given color are ever higher than the maxes supplied.
    For all of the valid games, the game ID is added to the total.

    Parameters
    ----------
    games : str[]
        A list of strings representing a game.
        e.g. "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

    Returns
    ------
    int
        The sum of the valid game IDs.
    """
    maxes = {"red": 12, "green": 13, "blue": 14}
    res = 0
    for game in games:
        rounds = game.split(": ")[1].split("; ")
        possible = True
        # Make sure a single value is never higher than the max value for a color
        for i, round in enumerate(rounds):
            cubes = round.split(", ")
            for cube in cubes:
                count, color = cube.split(" ")
                if int(count) > maxes[color]:
                    possible = False
                    break
            if not possible:
                break
        # If all the values are legit, add the game ID to the total
        if possible:
            res += i + 1
    return res


def part_two(games: list[str]) -> int:
    """
    Looks through the games played and finds the highest count of each cube per game.
    For all of the valid games, the product of each highest count is added to the total.

    Parameters
    ----------
    games : str[]
        A list of strings representing a game.
        e.g. "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

    Returns
    ------
    int
        The total of the product of each game's highest cube count per color.
    """
    res = 0
    for game in games:
        rounds = game.split(": ")[1].split("; ")
        needs = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }
        # Find the max value of each color that appears in a given around
        for round in rounds:
            cubes = round.split(", ")
            for cube in cubes:
                count, color = cube.split(" ")
                needs[color] = max(needs[color], int(count))
        # Add the product of the maxes to the total
        res += prod(needs.values())
    return res


def solve_puzzle(input_filepath: str) -> None:
    """
    Solves the second day puzzle for Advent of Code 2023: https://adventofcode.com/2023/day/2

    Parameters
    ----------
    input_filepath : str
        The filepath to the puzzle input.
    """
    games = Path(input_filepath).read_text().splitlines()
    print(f"Part one: {part_one(games)}")
    print(f"Part two: {part_two(games)}")


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    solve_puzzle(filepath)
