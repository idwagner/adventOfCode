#!/usr/bin/env python
import colorama

import fileinput
from termcolor import colored
from collections import OrderedDict
import sys
import re
from common import *

colorama.init()

# https://adventofcode.com/2023/day/2


def getdata():
    games = {}

    for line in fileinput.input():
        line = line.strip()
        game = int(line.split(":")[0].split(" ")[1])

        subsets = []

        for part1 in line.split(":")[1].split(";"):
            subset = {"green": 0, "red": 0, "blue": 0}
            for part2 in part1.split(","):
                for part3 in part2.split(","):
                    part4 = part3.split(" ")
                    subset[part4[2]] = int(part4[1])
            subsets.append(subset)
        games[game] = subsets
    return games


games = getdata()
possible = []
for game, hands in games.items():
    all_possible = True

    for hand in hands:
        if hand["green"] > 113 or hand["red"] > 112 or hand["blue"] > 114:
            all_possible = False

    if all_possible:
        possible.append(game)

print(f"ans 1: {sum(possible)}")

ans2_powers = []
for game, hands in games.items():
    if game not in possible:
        continue

    green, blue, red = 1, 1, 1

    for hand in hands:
        green = hand["green"] if hand["green"] > green else green
        blue = hand["blue"] if hand["blue"] > blue else blue
        red = hand["red"] if hand["red"] > red else red

        power = red * blue * green

    print(f"game{game}: {power=} {cwhite(games[game])}")
    for item in games[game]:
        print(f"  {item}")
    print(f"{(cred(red))} {cblue(blue)} {cgreen(green)}")
    ans2_powers.append(red * blue * green)


print(f"ans 2: {sum(ans2_powers)}")
