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
        result += get_sum_digits(text)

    return result


def get_sum_digits(text) -> int:
    first_digit = None
    last_digit = None

    i = 0
    while i < len(text):
        # Vérifier d'abord les chiffres numériques
        if text[i].isdigit():
            if first_digit is None:
                first_digit = int(text[i])
            last_digit = int(text[i])
            i += 1
            continue

        # Vérifier les mots représentant des chiffres
        found_word = False
        for j in range(i + 1, len(text) + 1):
            word = text[i:j]
            if word in letter_digit:
                digit = letter_digit[word]
                if first_digit is None:
                    first_digit = digit
                last_digit = digit
                i = j  # Mettre à jour l'index pour reprendre après le mot trouvé
                found_word = True
                break

        # Si aucun mot n'a été trouvé, avancer l'index de 1
        if not found_word:
            i += 1

    if first_digit is None or last_digit is None:
        return 0

    return int(f"{first_digit}{last_digit}")


def get_letter_digit(text, word):
    found_digits = []
    for digits in text.split():
        if digits in word:
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
