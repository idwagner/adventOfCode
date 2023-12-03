#!/usr/bin/env python
from colorama import just_fix_windows_console
import fileinput
from termcolor import colored
from collections import OrderedDict
import sys
import re

just_fix_windows_console()

# https://adventofcode.com/2023/day/1


def red(word):
    return colored(word, "red")


def green(word):
    return colored(word, "green")


def white(word):
    return colored(word, "white")


def backwards(word):
    return "".join(word[x] for x in sorted(range(0, len(word)), reverse=True))


def ans1():
    count = 0
    for line in fileinput.input():
        nums = [x for x in line if ord(x) >= 48 and ord(x) <= 57]
        strval = nums[0] + nums[-1]
        intval = int(strval)
        count += intval

    print(count)


def first_match(word, words):
    match_string = "(" + "|".join(words.keys()) + ")"
    matcher = re.compile(match_string)

    split = matcher.split(word)
    matching_ind = [i for i, x in enumerate(split) if x in words]
    return split[matching_ind[0]]


def ans2():
    words_fwd = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
    }
    words_bwd = {backwards(k): v for k, v in words_fwd.items()}

    count = 0
    for line in fileinput.input():
        line = line.strip().lower()
        backward = backwards(line)

        first = first_match(line, words_fwd)
        last = first_match(backward, words_bwd)

        value = words_fwd[first] * 10 + words_bwd[last]

        print(f"{white(first)} {white(backwards(last))} {green(line)} {white(value)}")

        count += value
    print(count)


ans2()
