#!/usr/bin/env python
import fileinput
from termcolor import colored
import sys
import re


def cred(word):
    return colored(word, "red")


def cgreen(word):
    return colored(word, "green")


def cblue(word):
    return colored(word, "blue")


def cwhite(word):
    return colored(word, "white")


def cyellow(word):
    return colored(word, "cyellow")


def backwards(word):
    return "".join(word[x] for x in sorted(range(0, len(word)), reverse=True))
