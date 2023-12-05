import os.path
from sys import argv


def gen_num_indexes_around(number):
    start = number['start']
    end = number['end']

    return {(x, y) for x in range(start[0] - 1, end[0] + 2) for y in range(start[1] - 1, end[1] + 2)}


def gen_indexes_tight(number):
    start = number['start']
    end = number['end']

    return {(x, y) for x in range(start[0], end[0] + 1) for y in range(start[1], end[1] + 1)}


def gen_gear_indexes(gear):
    return {(x, y) for x in range(gear[0] - 1, gear[0] + 2) for y in range(gear[1] - 1, gear[1] + 2)}


def gear_product(numbers):
    gears = {symbol['location'] for symbol in symbols if symbol['symbol'] == '*'}
    gear_indexes = [gen_gear_indexes(gear) for gear in gears]
    numbers_near_gears = [[number['number'] for number in numbers if gen_indexes_tight(number) & number_gear] for
                          number_gear in gear_indexes]
    product = [pair[0] * pair[1] for pair in numbers_near_gears if len(pair) == 2]
    return sum(product)


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
                    symbols += [{'symbol': element, 'location': (x, y)}]

                if num_start is not None:
                    numbers += [{'number': int(num_str), 'start': num_start, 'end': (x, y - 1)}]
                    num_start = None
                    num_str = ''

        if num_start is not None:
            numbers += [{'number': int(num_str), 'start': num_start, 'end': (x, len(row) - 1)}]
            num_start = None
            num_str = ''

    all_symbol_coords = {symbol['location'] for symbol in symbols}
    matches = [number['number'] for number in numbers if gen_num_indexes_around(number) & all_symbol_coords]

    print('Part 1', sum(matches))

    print('Part 2:', gear_product(numbers))
