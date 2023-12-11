import re
from collections import defaultdict


def resolver(filename):
    with open(filename, 'r') as file:
        text = file.read()

    return get_total_valid_game_numbers(text)


def process_text(text):
    parts = re.split(r'(Game \d+:)|;', text)
    parts = [part.strip() for part in parts if part and part.strip()]

    return parts


def is_line_valid(color_totals):
    max_red = 12
    max_green = 13
    max_blue = 14

    if color_totals['red'] > max_red or color_totals['green'] > max_green or color_totals['blue'] > max_blue:
        return False

    return True


def extract_game_number(line):
    match = re.search(r'Game (\d+):', line)

    return int(match.group(1)) if match else 0


def process_line(parts):
    line_color_totals = defaultdict(int)
    valid_subpart_count = 0

    for part in parts:
        part_color_totals = calculate_color_totals(part)

        for color, total in part_color_totals.items():
            line_color_totals[color] += total

        if is_line_valid(part_color_totals):
            valid_subpart_count += 1

    return valid_subpart_count


def get_total_valid_game_numbers(text):
    lines = text.split('\n')
    total_valid_subpart = 0

    for line in lines:
        game_number = extract_game_number(line)
        parts = process_text(line)
        valid_subpart = process_line(parts)

        if valid_subpart == len(parts):  # Si toutes les sous-parties sont valides
            total_valid_subpart += game_number

    return total_valid_subpart


def calculate_color_totals(part):
    color_totals = defaultdict(int)
    matches = re.findall(r'(\d+) (\w+)', part)
    for match in matches:
        number, color = match
        color_totals[color] += int(number)

    return color_totals
