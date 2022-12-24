"""day 20 solution from internet
source - https://github.com/Gravitar64/Advent-of-Code-2020
"""
import sys
import operator
from functools import reduce
from collections import defaultdict
import time
import re
import math


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


def read_puzzle(file):
    with open(file) as f:
        return [[x for x in tile.split("\n") if len(x) != 0] for tile in f.read().split("\n\n")]


def get_borders(tile):
    borders = [tile[1], tile[-1], tile[1][::-1], tile[-1][::-1]]
    left = right = ""
    for zeile in tile:
        if zeile[0] == "T":
            continue
        left += zeile[0]
        right += zeile[-1]
    borders.extend([left, right, left[::-1], right[::-1]])
    return borders


def solve(puzzle):
    bord_dict = defaultdict(list)
    for tile in puzzle:
        id = int(re.findall(r"\d+", tile[0])[0])
        borders = get_borders(tile)
        for b in borders:
            bord_dict[b].append(id)
    combos = defaultdict(set)
    for ids in bord_dict.values():
        if len(ids) < 2:
            continue
        combos[ids[0]].add(ids[1])
        combos[ids[1]].add(ids[0])
    return prod([id for id, ids in combos.items() if len(ids) == 2])


puzzle = read_puzzle(sys.argv[1])
# print(puzzle)
start = time.perf_counter()
print(solve(puzzle), time.perf_counter() - start)
