import math
import os.path
from collections import OrderedDict
from enum import Enum
from sys import argv


class State(Enum):
    SEEDS_TO_SOIL = 'seed-to-soil map:'
    SOIL_TO_FERTILIZER = 'soil-to-fertilizer map:'
    FERTILIZER_TO_WATER = 'fertilizer-to-water map:'
    WATER_TO_LIGHT = 'water-to-light map:'
    LIGHT_TO_TEMPERATURE = 'light-to-temperature map:'
    TEMPERATURE_TO_HUMIDITY = 'temperature-to-humidity map:'
    HUMIDITY_TO_LOCATION = 'humidity-to-location map:'
    END = 'end'


next_states = OrderedDict([
    (State.SEEDS_TO_SOIL, State.SOIL_TO_FERTILIZER),
    (State.SOIL_TO_FERTILIZER, State.FERTILIZER_TO_WATER),
    (State.FERTILIZER_TO_WATER, State.WATER_TO_LIGHT),
    (State.WATER_TO_LIGHT, State.LIGHT_TO_TEMPERATURE),
    (State.LIGHT_TO_TEMPERATURE, State.TEMPERATURE_TO_HUMIDITY),
    (State.TEMPERATURE_TO_HUMIDITY, State.HUMIDITY_TO_LOCATION),
    (State.HUMIDITY_TO_LOCATION, State.END)
])


def parse_file(fp):
    seed_mappings = {}
    seeds = []

    state = None
    for line in fp.readlines():
        line = line.strip()

        if not line:
            continue

        elif line.startswith('seeds:'):
            seeds = [int(v) for v in line.removeprefix('seeds: ').split(' ')]

        elif line.endswith(' map:'):
            state = State(line)

        else:
            dest_start, source_start, count = [int(number) for number in line.split(' ')]
            seed_mappings.setdefault(state, {})[(source_start, source_start + count)] = dest_start

    return seeds, seed_mappings


def find_min_location(seeds, seed_mappings):
    min_location = math.inf

    for seed in seeds:
        chain = [seed]
        current = seed
        for state in next_states.keys():
            curr_map = seed_mappings[state]
            next_num = next(
                (curr_map[(start, end)] + current - start for start, end in curr_map if start <= current <= end),
                current)
            chain += [next_num]
            current = next_num

        min_location = min(chain[-1], min_location)

    return min_location


def main():
    with open(os.path.join(os.path.dirname(__file__), argv[1])) as fp:
        seeds, seed_mappings = parse_file(fp)

        min_location = find_min_location(seeds, seed_mappings)
        print('Part 1:', min_location)

        seeds_expanded = list(range(seeds[0], seeds[0] + seeds[1])) + list(range(seeds[2], seeds[2] + seeds[3]))
        min_location = find_min_location(seeds_expanded, seed_mappings)
        print('Part 2:', min_location)


if __name__ == '__main__':
    main()
