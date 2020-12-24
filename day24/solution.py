#!/usr/bin/env python
# coding: utf-8
from collections import defaultdict
from copy import deepcopy
from typing import Dict, List, Tuple

print('--- Day 24: Lobby Layout ---')


DIRECTION_TO_COORDINATE_CHANGE = {
    'e': (1, 0, -1),
    'se': (0, 1, -1),
    'sw': (-1, 1, 0),
    'w': (-1, 0, 1),
    'nw': (0, -1, 1),
    'ne': (1, -1, 0)
}


# read the input data from `input.txt` into a list `tiles_directions`
tiles_directions = []
with open('input.txt', 'r') as f:
    for line in f:
        steps = []
        tmp = ''
        for c in line.rstrip('\n'):
            if c in {'n', 's'}:
                tmp += c
            else:
                tmp += c
                steps.append(tmp)
                tmp = ''
        tiles_directions.append(steps)


# part one
print('--- Part One ---')
tiles = defaultdict(lambda: 'white')
for directions in tiles_directions:
    q, r, s = (0, 0, 0)  # center coordinate
    for direction in directions:
        dq, dr, ds = DIRECTION_TO_COORDINATE_CHANGE[direction]
        q += dq
        r += dr
        s += ds
    tiles[(q, r, s)] = 'black' if tiles[(q, r, s)] == 'white' else 'white'
print(f'The number of tiles are left with the black side up is: {sum(color == "black" for color in tiles.values())}')


# part two
print('--- Part Two ---')
# define a function to get the neighbors (directly adjacent) of a tile
def get_neighbors(q: int, r: int, s: int) -> List[Tuple[int, int, int]]:
    return [(q+dq, r+dr, s+ds) for dq, dr, ds in DIRECTION_TO_COORDINATE_CHANGE.values()]
# define a function to update the tiles
def update_tiles(_tiles: Dict[Tuple[int, int, int], str]) -> Dict[Tuple[int, int, int], str]:
    # add neighbors (if not yet in `_tiles`)
    for tile in list(_tiles.keys()):
        for neighbor in get_neighbors(*tile):
            if neighbor not in _tiles:
                _tiles[neighbor] = 'white'
    # update tiles
    tiles = deepcopy(_tiles)
    for tile, color in list(_tiles.items()):
        neighbors = get_neighbors(*tile)
        neighbor_colors = [_tiles[neighbor] for neighbor in neighbors]
        if color == 'black':  # black tile
            if neighbor_colors.count('black') == 0 or neighbor_colors.count('black') > 2:  # flip to white
                tiles[tile] = 'white'
        if color == 'white':  # white tile
            if neighbor_colors.count('black') == 2:  # flip to black
                tiles[tile] = 'black'
    return tiles
# execute process 100 times
for _ in range(100):
    tiles = update_tiles(tiles)
print(f'The number of tiles are black after 100 days is: {sum(color == "black" for color in tiles.values())}')
