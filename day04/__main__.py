import os.path
from sys import argv


def parse(line):
    _, tickets = line.strip().split(': ')
    winning, playing = tickets.split(' | ')
    return convert_to_int(winning) & convert_to_int(playing)


def convert_to_int(numbers):
    split_nums = numbers.split(' ')
    return {int(number) for number in split_nums if number.isdigit()}


with open(os.path.join(os.path.dirname(__file__), argv[1])) as fp:
    matches = [parse(line) for line in fp.readlines()]
    scores = [pow(2, len(match) - 1) for match in matches if match]
    print('Part 1:', sum(scores))
