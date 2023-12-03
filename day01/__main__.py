import os.path
from sys import argv
import regex

translation = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
}

pattern = '(one|two|three|four|five|six|seven|eight|nine|[0-9])'


def numbers(line):
    first = translation[regex.findall(pattern, line)[0]]
    last = translation[regex.findall(pattern, line, flags=regex.REVERSE)[0]]
    return int(first + last)


with open(os.path.join(os.path.dirname(__file__), argv[1])) as fp:
    values = [numbers(line) for line in fp.readlines()]
    print(sum(values))
