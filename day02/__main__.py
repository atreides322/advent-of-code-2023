import os.path
from sys import argv

MAX = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def valid(cubes):
    parts = cubes.split(' ')
    return int(parts[0]) <= MAX[parts[1]]


def parse(line):
    label, games = line.strip().split(': ', 2)
    games = [game.split(', ') for game in games.split('; ')]
    possible = all(all([valid(color) for color in game]) for game in games)

    return int(label.split(' ')[1]) if possible else 0


with open(os.path.join(os.path.dirname(__file__), argv[1])) as fp:
    values = [parse(line) for line in fp.readlines()]
    print(sum(values))
