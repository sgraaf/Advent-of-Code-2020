#!/usr/bin/env python
# coding: utf-8
from functools import reduce
from itertools import count
from operator import mul
from typing import List, Tuple

print('--- Day 3: Toboggan Trajectory ---')

# read the input data from `input.txt` into a list `l`
l = [line.rstrip('\n') for line in open('input.txt', 'r')]

# compute the length and width of our grid
length = len(l)
width = len(l[0])

# define a function to compute the number of trees encountered
def compute_num_trees_encountered(slope: Tuple) -> int:
    slope_right, slope_down = slope
    return sum([l[i][j % width] == '#' for i, j in zip(range(slope_down, length, slope_down), count(slope_right, slope_right))])

# part one
print('--- Part One ---') 
slope = (3, 1)
print(f'Number of trees encountered: {compute_num_trees_encountered(slope)}')

# part two
print('--- Part Two ---')
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(f'Number of trees encountered: {reduce(mul, [compute_num_trees_encountered(slope) for slope in slopes])}')
