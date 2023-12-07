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

the_diagram = {}
seeds = []

with open(os.path.join(os.path.dirname(__file__), argv[1])) as fp:
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
            the_diagram.setdefault(state, {})[(source_start, source_start + count)] = dest_start

min_location = math.inf

for seed in seeds:
    chain = [seed]
    current = seed
    for state in next_states.keys():
        curr_map = the_diagram[state]
        next_num = next(
            (curr_map[(start, end)] + current - start for start, end in curr_map if start <= current <= end),
            current)
        chain += [next_num]
        current = next_num

    min_location = min(chain[-1], min_location)

print('Part 1:', min_location)
