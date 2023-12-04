#!/usr/bin/env python
import colorama

from pprint import pprint
import fileinput
from termcolor import colored
from collections import OrderedDict
import sys
import re
from common import *

colorama.init()


def get_data():
    games = {}

    for line in fileinput.input():
        line = line.strip()
        game = int(line.split(":")[0].split(" ")[-1])
        card = [
            int(x.strip())
            for x in line.split(":")[1].split("|")[0].split(" ")
            if x.strip()
        ]
        winners = [
            int(x.strip())
            for x in line.split(":")[1].split("|")[1].split(" ")
            if x.strip()
        ]
        games[game] = (card, winners)

    return games


def ans1(games):
    values = []
    for card, winner in games.values():
        match_numbers = set(card).intersection(winner)
        score = 2 ** (len(match_numbers) - 1) if match_numbers else 0
        # print(f"{len(match_numbers)=} {match_numbers=} {score=}")
        values.append(score)
    return sum(values)


def game_winners(games):
    ret = {}
    for game, items in games.items():
        card, winner = items
        match_numbers = set(card).intersection(winner)
        ret[game] = len(match_numbers)

    return ret


def winner_copies(gamenum, wins):
    """Return list of the subsequent games from a winning card"""
    return [x for x in range(gamenum + 1, gamenum + wins + 1)]


def recursive_wins(gamenum):
    if gamenum in score_cache:
        return score_cache[gamenum]

    additional = winner_copies(gamenum, winner_chart[gamenum])
    score = len(additional)
    for child_gamenum in winner_copies(gamenum, winner_chart[gamenum]):
        score += recursive_wins(child_gamenum)

    score_cache[gamenum] = score
    return score


def ans2(games):
    score = 0

    for gamenum in sorted(winner_chart.keys()):
        score += recursive_wins(gamenum)

    return score + len(games)


games = get_data()
winner_chart = game_winners(games)
score_cache = {}

# print(f"ans1: {ans1(games)}")
print(f"ans2: {ans2(games)}")
