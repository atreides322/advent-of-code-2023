import os.path
from sys import argv

with open(os.path.join(os.path.dirname(__file__), argv[1])) as fp:
    numbers = [[digit for digit in line if digit.isdigit()] for line in fp.readlines()]
    cal_value = [int(line[0] + line[-1]) for line in numbers]
    print(sum(cal_value))
