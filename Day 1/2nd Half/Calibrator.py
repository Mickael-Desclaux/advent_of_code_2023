import typing


def calibrator():
    puzzle = []
    with open("data.txt", 'r') as file:
        for line in file:
            puzzle.append(line.strip())

    found_digits = []
    for line in puzzle:
        found_digits.extend(get_letter_digit(line, letter_digit))

    return found_digits


def get_sum_result(data: typing.List[str]) -> int:
    result = 0
    for text in data:
        result += get_sum_digits(text)

    return result


def get_sum_digits(text) -> int:
    first_digit = None
    last_digit = None

    for character in text:
        if character.isdigit():  # if character.isdigit() or found_digit
            if first_digit is None:
                first_digit = character
            last_digit = character

    sum_result = first_digit + last_digit

    return int(sum_result)


def get_letter_digit(text, word):
    found_digits = []
    for digits in word.keys():
        if digits in text:
            found_digits.append(word[digits])

    return found_digits


letter_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
