import functools
import itertools
import operator
import os.path
from sys import argv

MAX = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def parse_color(color):
    parts = color.split(' ')
    return parts[1], int(parts[0])


def parse(line):
    label, games = line.strip().split(': ', 2)
    number = int(label.split(' ')[1])
    games = [game.split(', ') for game in games.split('; ')]
    games = [dict(parse_color(color) for color in game) for game in games]
    return number, games


def valid_draw(color, count):
    return count <= MAX[color]


def valid_game(rounds):
    return all(all(valid_draw(color, count) for color, count in round_.items()) for round_ in rounds)


def min_required(rounds):
    flattened = [(k, v) for round_ in rounds for k, v in round_.items()]
    grouped = itertools.groupby(sorted(flattened), lambda x: x[0])
    return {k: max([num for (_, num) in v]) for k, v in grouped}


with (open(os.path.join(os.path.dirname(__file__), argv[1])) as fp):
    games = [parse(line) for line in fp.readlines()]
    values = [(num, valid_game(rounds)) for num, rounds in games]
    total = sum(num for num, valid in values if valid)
    print('Part 1:', total)

    required = [min_required(rounds) for _, rounds in games]
    powers = [functools.reduce(operator.mul, game.values()) for game in required]
    print('Part 2:', sum(powers))
