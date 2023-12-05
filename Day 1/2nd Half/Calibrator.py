import typing


def calibrator():
    puzzle = []
    with open("data.txt", 'r') as file:
        for line in file:
            puzzle.append(line.strip())

    return get_sum_result(puzzle)


def get_sum_result(data: typing.List[str]) -> int:
    result = 0
    for text in data:
        result += get_sum_digits(text, letter_digit)

    return result


# def get_sum_digits(text) -> int:
#     first_digit = None
#     last_digit = None
#     last_word_start_index = None  # Ajouter un index pour mémoriser le début du dernier mot trouvé
#
#     i = 0
#     while i < len(text):
#         # Vérifier d'abord les chiffres numériques
#         if text[i].isdigit():
#             if first_digit is None:
#                 first_digit = int(text[i])
#             last_digit = int(text[i])
#             last_word_start_index = None  # Réinitialiser le début du dernier mot trouvé
#             i += 1
#             continue
#
#         # Vérifier les mots représentant des chiffres
#         found_word = False
#         for j in range(i + 1, len(text) + 1):
#             word = text[i:j]
#             if word in letter_digit:
#                 digit = letter_digit[word]
#                 if first_digit is None:
#                     first_digit = digit
#                 last_digit = digit
#                 if last_word_start_index is None or i > last_word_start_index:
#                     last_word_start_index = i
#                 found_word = True
#                 break
#
#         # Si un mot est trouvé, recommencer la recherche à partir du caractère suivant le début de ce mot
#         if found_word:
#             i = last_word_start_index + 1
#         else:
#             i += 1
#
#     if first_digit is None or last_digit is None:
#         return 0
#
#     return int(f"{first_digit}{last_digit}")


# def get_letter_digit(text, word):
#     found_digits = []
#     for digits in text.split():
#         if digits in word:
#             found_digits.append(word[digits])
#
#     return found_digits


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


def get_first_last_digit(text: str) -> tuple:
    digits = [char for char in text if char.isdigit()]
    if not digits:
        return None, None
    return int(digits[0]), int(digits[-1])


def get_letter_digit(text: str, letter_digit: dict) -> tuple:
    words = text.split()
    first_digit = None
    last_digit = None
    for word in words:
        try:
            if word in letter_digit:
                digit = letter_digit[word]
                if first_digit is None:
                    first_digit = digit
                last_digit = digit
        except ValueError:
            continue

    return first_digit, last_digit


def get_sum_digits(text: str, letter_digit: dict) -> int:
    first_digit, last_digit = get_first_last_digit(text)
    if first_digit is None or last_digit is None:
        first_digit, last_digit = get_letter_digit(text, letter_digit)

    if first_digit is None or last_digit is None:
        return 0

    return int(f"{first_digit}{last_digit}")
