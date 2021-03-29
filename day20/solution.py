#!/usr/bin/env python
# coding: utf-8
import re
from collections import defaultdict
from typing import List, Optional, Tuple
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
    return [(x + i, y + j) for i in (-1, 0) for j in (-1, 0) if x + i >= 0 and y + j >= 0 and bool(i) ^ bool(j)]

def count_hashtag(tile: List[str]):
    return sum(row.count('#') for row in tile)
    

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
SEAMONSTER_PATTERN = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]
PATTERN_HEIGHT = len(SEAMONSTER_PATTERN)
PATTERN_WIDTH = len(SEAMONSTER_PATTERN[0])

# get the IDs of the edge and center tiles
edges = [ID for ID, IDs in ID_to_IDs.items() if len(IDs) == 3]
center = [ID for ID, IDs in ID_to_IDs.items() if len(IDs) > 3]
# compute the image height and width
height = width = int(len(ID_to_tile) ** 0.5)

loc_to_ID = {}
ID_to_loc = {}
loc_to_tile = {}

# place the first corner tile
row, col = 0, 0
ID = corners[0]
orientations = get_orientations(ID_to_tile[ID])
neighbor_IDs = ID_to_IDs[ID]
shared_borders = set.union(*[IDs_to_border[(ID, neigbor_ID)] for neigbor_ID in neighbor_IDs])
for orientation in orientations:
    if right_border(orientation) in shared_borders and bottom_border(orientation) in shared_borders:  # orientation match
        loc_to_ID[(row, col)] = ID
        ID_to_loc[ID] = (row, col)
        loc_to_tile[(row, col)] = orientation
        break

# place the remaining tiles
for row, col in product(range(height), range(width)):
    if (row, col) == (0, 0):  # skip the first corner tile
        continue
    # get the neighbors
    neighbor_locs = find_neighbors(row, col)
    neighbor_tiles = [loc_to_tile[loc] for loc in neighbor_locs]
    # get the candidate IDs
    cancidate_IDs = set.union(*[ID_to_IDs[loc_to_ID[loc]] for loc in neighbor_locs]) - set(ID_to_loc.keys())
    for ID in cancidate_IDs:
        orientations = get_orientations(ID_to_tile[ID])
        for orientation in orientations:
            for loc, tile in zip(neighbor_locs, neighbor_tiles):
                if loc[0] == row:  # left neighbor
                    if not right_border(tile) == left_border(orientation):
                        break
                else:  # top neighbor
                    if not bottom_border(tile) == top_border(orientation):
                        break
            else:  # orientation match
                loc_to_ID[(row, col)] = ID
                ID_to_loc[ID] = (row, col)
                loc_to_tile[(row, col)] = orientation
                break
        else:
            continue
        break

# remove the borders
for loc, tile in loc_to_tile.items():
    loc_to_tile[loc] = [row[1:-1] for row in tile[1:-1]]

# stitch the tiles together into a single image
image = []
for row in range(height):
    for _row in range(len(loc_to_tile[row, 0])):
        image.append(''.join([loc_to_tile[row, col][_row] for col in range(width)]))

# try all orientations of the image to find the seamonsters
image_orientations = get_orientations(image)
for image_orientation in image_orientations:
    seamonster_count = 0
    for i in range(len(image_orientation) - PATTERN_HEIGHT + 1):
        for j in range(len(image_orientation[i]) - PATTERN_WIDTH + 1):
            for x in range(PATTERN_WIDTH):
                for y in range(PATTERN_HEIGHT):
                    if SEAMONSTER_PATTERN[y][x] == '#':
                        if not image_orientation[i + y][j + x] == '#':
                            break
                else:
                    continue
                break
            else:
                seamonster_count += 1
    if seamonster_count > 0:
        break

print(f'The number of # that are not part of a sea monster is: {count_hashtag(image_orientation) - seamonster_count * count_hashtag(SEAMONSTER_PATTERN)}')
