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


neighbors = [
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


def find_numbers(hline):
    ret = []
    matches = re_numbers.split(hline)
    if not matches[0]:
        matches.pop(0)

    if matches[-1] == None:
        matches.pop(-1)


def is_symbol(char) -> bool:
    if char in "0123456789.":
        return False
    return True


def has_symbol_neighbor(lines, hpos, vpos) -> bool:
    for h_offset, v_offset in neighbors:
        if not 0 <= hpos + h_offset < len(lines[vpos]):
            continue

        if not 0 <= vpos + v_offset < len(lines):
            continue

        try:
            if is_symbol(lines[v_offset + vpos][h_offset + hpos]):
                return True
        except:
            print()
            print(f"{line}")

            print(f"{v_offset=} {h_offset=} {hpos=} {vpos=}")
            raise


data = getdata()
with_neighbors = []
for vpos, line in enumerate(data):
    found_symbol = False
    symbol_neighbor = False

    reset_number = False
    series_len = 0

    for hpos, char in enumerate(line):
        if char in "1234567890":
            if has_symbol_neighbor(data, hpos, vpos):
                symbol_neighbor = True

            series_len += 1

        else:
            if not series_len:
                print(cgreen(char), end="")
                continue

            reset_number = True

        if reset_number and series_len:
            reset_number = False

            series_chars = "".join(
                [line[hpos - series_len + x] for x in range(0, series_len)]
            )

            number_value = int(series_chars)
            if symbol_neighbor:
                with_neighbors.append(number_value)
                print(cred(number_value), end="")
            else:
                print(cwhite(number_value), end="")

            print(cgreen(char), end="")

            series_len = 0
            symbol_neighbor = False
            series_chars = ""
    print()


print()
# print(with_neighbors)
print(sum(with_neighbors))
