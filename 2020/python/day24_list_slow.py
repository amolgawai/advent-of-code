'''Day 24 solution'''
import sys
import re
import operator
from collections import defaultdict


def parse_input(input_f_name):
    '''parses input from the given file name and returns data'''
    with open(input_f_name) as input_f:
        data = input_f.read().split('\n')

    # create and return data structure
    return data


dir_map = {'e': (1, 0),
           'se': (1, -1),
           'sw': (0, -1),
           'w': (-1, 0),
           'nw': (-1, 1),
           'ne': (0, 1)}


tiles_adjacents = defaultdict(list)


def get_adjacent_tiles(tile):
    """Gets the 6 adjacent tiles
    Keyword Arguments:
    tile -- the tile for wich we need surrounding tiles
    """

    adjcnts = list()
    if tile in tiles_adjacents.keys():
        return tiles_adjacents[tile]
    for delta in dir_map.values():
        adjcnts.append(tuple(map(operator.add, tile, delta)))

    tiles_adjacents[tile] = adjcnts
    return adjcnts


def flip_tiles(black_tiles):
    """Flips black and white tiles according to the rules
    Keyword Arguments:
    black_tiles -- list of black tiles
    """

    white_flip = set()
    white_seen = set()
    black_flip = set()
    for a_tile in black_tiles:
        adjcnt_lst = get_adjacent_tiles(a_tile)
        adcnt_whites = [tile for tile in adjcnt_lst if tile not in black_tiles]
        # adcnt_whites = get_adjacent_white_tiles_lst(a_tile, black_tiles)
        whts = len(adcnt_whites)
        if whts == 6 or whts < 4:
            black_flip.add(a_tile)

        for a_white in adcnt_whites:
            if a_white not in white_seen:
                white_seen.add(a_white)
                whit_adjacent = 0
                for w_adjcnt in get_adjacent_tiles(a_white):
                    if w_adjcnt in black_tiles:
                        whit_adjacent += 1

                if whit_adjacent == 2:
                    white_flip.add(a_white)

    flipped = [tile for tile in black_tiles if tile not in black_flip]
    flipped.extend(white_flip)
    return flipped


def main(input_f_name):
    '''The main function'''
    data_struct = parse_input(input_f_name)
    instr_list = list()
    for line in data_struct:
        instr_list.append(list(filter(None,
                                      re.split('(e|se|sw|w|nw|ne)', line))))

    instr_list = list(filter(None, instr_list))
    black_tiles = list()
    for instrs in instr_list:
        tile = (0, 0)
        for instr in instrs:
            tile = tuple(map(operator.add, tile, dir_map[instr]))

        if tile not in black_tiles:
            black_tiles.append(tile)
        else:
            black_tiles.remove(tile)

    print(len(black_tiles))

    flipped_tiles = black_tiles
    for __ in range(100):
        flipped_tiles = flip_tiles(flipped_tiles)

    print(len(flipped_tiles))


if __name__ == '__main__':
    main(sys.argv[1])
