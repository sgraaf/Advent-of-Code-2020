#!/usr/bin/env python
# coding: utf-8
from collections import defaultdict
from copy import deepcopy
from itertools import product
from typing import Dict, List, Tuple

print('--- Day 17: Conway Cubes ---')

# the number of cycles to simulate
NUM_CYCLES = 6

# read the input data from `input.txt` into dicts `grid_1` and `grid_2` (for parts one and two, respectively)
grid_1 = defaultdict(lambda: '.')
grid_2 = defaultdict(lambda: '.')
x = y = z = w = 0
with open('input.txt', 'r') as f:
    for line in f:
        for cube in line.rstrip('\n'):
            grid_1[(x, y, z)] = cube
            grid_2[(x, y, z, w)] = cube
            y += 1
        x += 1
        y = 0  # reset y

# part one
print('--- Part One ---')
# defines a function to find the neighbors of a cube in our 3-dimensional grid
def find_neighbors_1(x: int, y: int, z: int) -> List[Tuple[int, int, int]]:
    return [(x + i, y + j, z + k) for i in (-1, 0, 1) for j in (-1, 0, 1) for k in (-1, 0, 1) if not (i == j == k == 0)]

# defines a function to find the dimensions of our "infinite" 3-dimensional grid
def find_dimensions_1(grid: Dict[Tuple[int, int, int], str]) -> Tuple[Tuple[int, int]]:
    xs, ys, zs = zip(*grid.keys())
    return (min(xs), max(xs)), (min(ys), max(ys)), (min(zs), max(zs))

# defines a function to apply an update cycle to our 3-dimensional grid
def update_grid_1(grid: Dict[Tuple[int, int, int], str]) -> None:
    out_grid = deepcopy(grid)
    (x_min, x_max), (y_min, y_max), (z_min, z_max) = find_dimensions_1(grid)
    for x, y, z in product(range(x_min - 1, x_max + 2), range(y_min - 1, y_max + 2), range(z_min - 1, z_max + 2)):
        neighbors = find_neighbors_1(x, y, z)
        if grid[(x, y, z)] == '#':  # active
            if sum(grid[(i, j, k)] == '#' for i, j, k in neighbors) not in {2, 3}:  # not exactly 2 or 3 active neighbors
                out_grid[(x, y, z)] = '.'  # update cube to inactive
        elif grid[(x, y, z)] == '.':  # inactive
            if sum(grid[(i, j, k)] == '#' for i, j, k in neighbors) == 3:  # exactly 3 active neighbors
                out_grid[(x, y, z)] = '#'  # update cube to active
    return out_grid

# iteratively apply the update cycle to our 3-dimensional grid
for _ in range(NUM_CYCLES):
    grid_1 = update_grid_1(grid_1)
print(f'The number of cubes left in the active state after the sixth cycle is: {list(grid_1.values()).count("#")}')


# part two
print('--- Part Two ---')
# defines a function to find the neighbors of a cube in our 4-dimensional grid
def find_neighbors_2(x: int, y: int, z: int, w: int) -> List[Tuple[int, int, int, int]]:
    return [(x + i, y + j, z + k, w + l) for i in (-1, 0, 1) for j in (-1, 0, 1) for k in (-1, 0, 1) for l in (-1, 0, 1) if not (i == j == k == l == 0)]

# defines a function to find the dimensions of our "infinite" 4-dimensional grid
def find_dimensions_2(grid: Dict[Tuple[int, int, int, int], str]) -> Tuple[Tuple[int, int]]:
    xs, ys, zs, ws = zip(*grid.keys())
    return (min(xs), max(xs)), (min(ys), max(ys)), (min(zs), max(zs)), (min(ws), max(ws))

# defines a function to apply an update cycle to our 4-dimensional grid
def update_grid_2(grid: Dict[Tuple[int, int, int, int], str]) -> None:
    out_grid = deepcopy(grid)
    (x_min, x_max), (y_min, y_max), (z_min, z_max), (w_min, w_max) = find_dimensions_2(grid)
    for x, y, z, w in product(range(x_min - 1, x_max + 2), range(y_min - 1, y_max + 2), range(z_min - 1, z_max + 2), range(w_min - 1, w_max + 2)):
        neighbors = find_neighbors_2(x, y, z, w)
        if grid[(x, y, z, w)] == '#':  # active
            if sum(grid[(i, j, k, l)] == '#' for i, j, k, l in neighbors) not in {2, 3}:  # not exactly 2 or 3 active neighbors
                out_grid[(x, y, z, w)] = '.'  # update cube to inactive
        elif grid[(x, y, z, w)] == '.':  # inactive
            if sum(grid[(i, j, k, l)] == '#' for i, j, k, l in neighbors) == 3:  # exactly 3 active neighbors
                out_grid[(x, y, z, w)] = '#'  # update cube to active
    return out_grid

# iteratively apply the update cycle to our 4-dimensional grid
for _ in range(NUM_CYCLES):
    grid_2 = update_grid_2(grid_2)
print(f'The number of cubes left in the active state after the sixth cycle is: {list(grid_2.values()).count("#")}')
