import json
import os.path
from sys import argv


def gen_indexes(number):
    start = number['start']
    end = number['end']

    return {(x, y) for x in range(start[0] - 1, end[0] + 2) for y in range(start[1] - 1, end[1] + 2)}


with open(os.path.join(os.path.dirname(__file__), argv[1])) as fp:
    values = [list(line.strip()) for line in fp.readlines()]

    symbols = []
    numbers = []
    num_str = ''
    num_start = None

    for x, row in enumerate(values):
        for y, element in enumerate(row):
            if element.isdigit():
                if num_start is None:
                    num_start = (x, y)

                num_str += element
            else:
                if not (element == '.' or element.isalnum()):
                    symbols += [(x, y)]

                if num_start is not None:
                    numbers += [{'number': int(num_str), 'start': num_start, 'end': (x, y - 1)}]
                    num_start = None
                    num_str = ''

        if num_start is not None:
            numbers += [{'number': int(num_str), 'start': num_start, 'end': (x, len(row) - 1)}]
            num_start = None
            num_str = ''

    symbols = set(symbols)

    matches = [number['number'] for number in numbers if gen_indexes(number) & symbols]

    print(sum(matches))
