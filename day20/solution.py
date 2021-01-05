#!/usr/bin/env python
# coding: utf-8
import re
from collections import defaultdict
from typing import List, Tuple
from operator import mul
from functools import reduce
from itertools import product

print('--- Day 20: Jurassic Jigsaw ---')

# read the input data from `input.txt` into a dict `tiles`
ID_to_tile = {}
with open('input.txt', 'r') as f:
    for tile in f.read().split('\n\n'):
        if tile != '':
            ID, *tile = tile.split('\n')
            ID = int(re.match(r'Tile (\d+):', ID).group(1))
            ID_to_tile[ID] = tile

def print_tile(tile: List[str]) -> None:
    for row in tile:
        print(''.join(row))

top_border = lambda tile: tile[0]
bottom_border = lambda tile: tile[-1]
left_border = lambda tile: ''.join([row[0] for row in tile])
right_border = lambda tile: ''.join([row[-1] for row in tile])

def rotateCW(tile: List[str]) -> List[str]:
    return [''.join([tile[len(tile) - i - 1][j] for i in range(len(tile))]) for j in range(len(tile))]

def flip(tile: List[str]) -> List[str]:
    return [row[::-1] for row in tile]

def get_orientations(tile: List[str]) -> List[List[str]]:
    orientations = [tile, flip(tile)]
    for _ in range(3):
        tile = rotateCW(tile)
        orientations += [tile, flip(tile)]
    return orientations

def get_borders(tile: List[str]) -> List[str]:
    borders = [top_border(tile), bottom_border(tile), left_border(tile), right_border(tile)]  # rotations
    borders += flip(borders)  # flips
    return borders

def find_neighbors(x: int, y: int) -> List[Tuple[int, int]]:
    return [(x + i, y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]
    

# part one
print('--- Part One ---')
# for each tile (ID), get its borders
ID_to_borders = {ID: get_borders(tile) for ID, tile in ID_to_tile.items()}
# for each border, see which tile IDs are associated with it
border_to_IDs = defaultdict(list)
for ID, borders in ID_to_borders.items():
    for border in borders:
        border_to_IDs[border].append(ID)
# connect each tile to the other tiles it shares a border with
ID_to_IDs = defaultdict(set)
IDs_to_border = defaultdict(set)
for border,IDs in border_to_IDs.items():
    if len(IDs) == 2:
        ID_1, ID_2 = IDs
        ID_to_IDs[ID_1].add(ID_2)
        ID_to_IDs[ID_2].add(ID_1)
        IDs_to_border[(ID_1, ID_2)].add(border)
        IDs_to_border[(ID_2, ID_1)].add(border)
# get the IDs of the corner tiles
corners = [ID for ID, IDs in ID_to_IDs.items() if len(IDs) == 2]
# compute the multiplication of the IDs of the corner tiles
print(f'The multiplication of the IDs of the four corner tiles is: {reduce(mul, corners)}')

# part two
print('--- Part Two ---')
# get the IDs of the edge and center tiles
edges = [ID for ID, IDs in ID_to_IDs.items() if len(IDs) == 3]
center = [ID for ID, IDs in ID_to_IDs.items() if len(IDs) > 3]
# compute the image height and width
height = width = int(len(ID_to_tile) ** 0.5)

loc_to_ID = {}
loc_to_tile = {}
for row, col in product(range(height), range(width)):
    if (row, col) == (0, 0):  # place the corner tile
        ID = corners[0]
        tile = ID_to_tile[ID]
        orientations = get_orientations(tile)
        neighbor_IDs = ID_to_IDs[ID]
        shared_borders = set.union(*[IDs_to_border[(ID, neigbor_ID)] for neigbor_ID in neighbor_IDs])
        for orientation in orientations:
            if right_border(orientation) in shared_borders and bottom_border(orientation) in shared_borders:  # correct orientation
                loc_to_ID[(row, col)] = ID
                loc_to_tile[(row, col)] = orientation
                break
        continue
    
    if row in {0, height - 1} and col in {0, width - 1}:  # corner
        for ID in corners:
            if ID not in loc_to_ID.values():
                neighbor_locs = [neighbor_loc for neighbor_loc in find_neighbors(row, col) if neighbor_loc in loc_to_ID]
                neighbor_IDs = [loc_to_ID[neighbor_loc] for neighbor_loc in neighbor_locs]
    elif row in {0, height - 1}:  # top / bottom edge
        for ID in edges:
            if ID not in loc_to_ID.values():
                pass
    elif col in {0, width - 1}:  # left / right edge
        for ID in edges:
            if ID not in loc_to_ID.values():
                pass
    else:  # center tile
        for ID in center:
            if ID not in loc_to_ID.values():
                pass
    for ID, tile in ID_to_tile.items():
        if ID not in loc_to_ID.values():
            if I
            if row in {0, height - 1}:  # top / bottom edge

            elif