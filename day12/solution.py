#!/usr/bin/env python
# coding: utf-8
from typing import Tuple
import re

print('--- Day 12: Rain Risk ---')

# define a mapping from direction (N, E, S and W) to dx, dy
DIRECTION_MAP = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}
# get a list of just the directions (i.e. N, E, S and W)
DIRECTIONS = [*DIRECTION_MAP]

# read the input data from `input.txt` into a list `navigation_instructions`
navigation_instructions = []
with open('input.txt', 'r') as f:
    for line in f:
        action, value = re.match(r'([NESWLRF])(\d+)', line).groups()
        navigation_instructions.append((action, int(value)))

# part one
print('--- Part One ---')
# define a function to perform rotations
def rotate(direction: str, degree: int) -> str:
    return DIRECTIONS[(DIRECTIONS.index(direction) + degree // 90) % len(DIRECTIONS)]

# starting position and direction
x, y = 0, 0
direction = 'E'

# follow all of the navigation instructions
for action, value in navigation_instructions:
    if action in {'N', 'E', 'S', 'W', 'F'}:  # move
        dx, dy = DIRECTION_MAP[direction if action == 'F' else action]
        x += dx * value
        y += dy * value
    elif action in {'L', 'R'}:  # rotate
        direction = rotate(direction, value * (-1 if action == 'L' else 1))
print(f'The Manhattan distance between the end location and the ship\'s starting position is {abs(x) + abs(y)}')


# part two
print('--- Part Two ---')
# (re-)define a function to perform rotations
def rotate2(x: int, y: int, degree: int) -> Tuple[int, int]:
    degree = (degree + 360) % 360
    if degree in {0, 360}:
        return x, y
    elif degree == 90:
        return y, -x
    elif degree == 180:
        return -x, -y
    elif degree == 270:
        return -y, x

# starting position of the ship and waypoint (relative)
x_ship, y_ship = 0, 0
x_wpt, y_wpt = 10, 1

# follow all of the navigation instructions
for action, value in navigation_instructions:
    if action in {'N', 'E', 'S', 'W'}:  # move the waypoint
        dx, dy = DIRECTION_MAP[direction if action == 'F' else action]
        x_wpt += dx * value
        y_wpt += dy * value
    elif action in {'L', 'R'}:  # rotate
        x_wpt, y_wpt = rotate2(x_wpt, y_wpt, value * (-1 if action == 'L' else 1))
    elif action == 'F':  # move the ship
        dx, dy = x_wpt, y_wpt
        x_ship += dx * value
        y_ship += dy * value
print(f'The Manhattan distance between the end location and the ship\'s starting position is {abs(x_ship) + abs(y_ship)}')
