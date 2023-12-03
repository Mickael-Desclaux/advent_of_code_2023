from typing import List


def calibrator():
    puzzle = []
    with open("Day 1/data.txt", 'r') as file:
        for line in file:
            puzzle.append(line.strip())

    return get_sum_result(puzzle)


def get_sum_result(data: List[str]) -> int:
    result = 0
    for text in data:
        result += get_sum_digits(text)

    return result


def get_sum_digits(text) -> int:
    first_digit = None
    last_digit = None

    for character in text:
        if character.isdigit():
            if first_digit is None:
                first_digit = character
            last_digit = character

    sum_result = first_digit + last_digit

    return int(sum_result)
