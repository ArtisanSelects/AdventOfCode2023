import os
from pathlib import Path


def part_one(lines: list[str]) -> int:
    """
    Looks through the characters in a string and finds the first and last digits.
    Then it turns those digits into a two digit number and adds it to the total.

    Parameters
    ----------
    lines : str[]
        A list of strings.
        e.g. pqr3stu8vwx

    Returns
    -------
    int
        The total of all two digit numbers found in each line.
    """
    res = 0
    for line in lines:
        for char in line:
            if char.isdigit():
                a = char
                break
        for char in reversed(line):
            if char.isdigit():
                res += int(a + char)
                break
    return res


def part_two(lines: list[str]) -> int:
    """
    Looks through the characters in a string and finds the first and last digits.
    The digits can be either 1-9 characters or the words "one", "two", etc.
    Then it turns those digits into a two digit number and adds it to the total.

    Parameters
    ----------
    lines : str[]
        A list of strings.
        e.g. abcone2threexyz

    Returns
    -------
    int
        The total of all two digit numbers found in each line.
    """
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    starters = set([i[0] for i in nums])
    res = 0
    # Could do the same as part one where we go in reverse after finding a hit, but this runs quick enough to solve the puzzle.
    for line in lines:
        line_nums = []
        for i, char in enumerate(line):
            if char.isdigit():
                line_nums.append(char)
                continue
            if char in starters:
                for j, num in enumerate(nums):
                    if line[i : i + (len(num))] == num:
                        line_nums.append(str(j + 1))
                        break
        res += int(line_nums[0] + line_nums[-1])
    return res


def solve_puzzle(input_filepath: str) -> None:
    """
    Solves the first day puzzle for Advent of Code 2023: https://adventofcode.com/2023/day/1

    Parameters
    ----------
    input_filepath : str
        The filepath to the puzzle input.
    """
    lines = Path(input_filepath).read_text().splitlines()
    print(f"Part one: {part_one(lines)}")
    print(f"Part two: {part_two(lines)}")


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    solve_puzzle(filepath)
