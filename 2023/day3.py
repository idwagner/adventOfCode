#!/usr/bin/env python
import colorama

import fileinput
from termcolor import colored
from collections import OrderedDict
import sys
import re
from common import *

colorama.init()

re_numbers = re.compile(r"([0-9]+)")
# https://adventofcode.com/2023/day/2


neighbors_grid = [
    [-1, -1],
    [0, -1],
    [1, -1],
    [-1, 0],
    [1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
]


def getdata():
    data = []

    for line in fileinput.input():
        line = line.strip()
        data.append(line + ".")

    return data


def is_symbol(char) -> bool:
    if char in "0123456789.":
        return False
    return True


def symbol_neighbors(lines, charset) -> bool:
    neighbors = set()
    y = charset[1]
    for i in range(0, len(str(charset[3]))):
        x = charset[0] + i
        for x_offset, y_offset in neighbors_grid:
            coord = (x + x_offset, y + y_offset)
            if not 0 <= x + x_offset < len(lines[y]):
                continue

            if not 0 <= y + y_offset < len(lines):
                continue

            if is_symbol(lines[y_offset + y][x_offset + x]):
                neighbors.add((y_offset + y, x_offset + x))

    return neighbors


all_neighbors = []
data = getdata()
series = []
for y, line in enumerate(data):
    x = 0
    while x <= len(line) - 1:
        if line[x] in "1234567890":
            st = x
            while True:
                x += 1
                if line[x] not in "1234567890":
                    break
            length = x - st
            value = line[st : length + st]
            series.append( [ st, y, length, int(value) ] )
            x -= 1
        x += 1


with_neighbors = []
for s in series:
    symbols = symbol_neighbors(data, s)

    if symbols:
        with_neighbors.append(s[3])

print(with_neighbors)
print(sum(with_neighbors))
