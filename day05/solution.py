#!/usr/bin/env python
# coding: utf-8
import re
from itertools import product
from typing import Tuple

print('--- Day 5: Binary Boarding ---')

# rows and columns of the seats on the plane
ROWS = list(range(128))
COLUMNS = list(range(8))

# read the input data from `input.txt` into a list `boarding_passes`
boarding_passes = [line.rstrip('\n') for line in open('input.txt', 'r').readlines()]

# part one
print('--- Part One ---')

# define a function to decode the boarding pass
def decode_boarding_pass(boarding_pass: str) -> Tuple[int, int]:
    rows, columns = ROWS, COLUMNS
    
    # parse the boarding pass
    row_directions, column_directions = re.search(r'([FB]{7})([LR]{3})', boarding_pass).groups()
    
    # get the row
    for row_direction in row_directions:
        rows = rows[:(len(rows)-1) // 2 + 1] if row_direction == 'F' else rows[len(rows) // 2:]
    row = rows[0]
    
    # get the column
    for column_direction in column_directions:
        columns = columns[:(len(columns)-1) // 2 + 1] if column_direction == 'L' else columns[len(columns) // 2:]
    column = columns[0]
    
    return row, column

# decode the boarding passes
seats = [decode_boarding_pass(boarding_pass) for boarding_pass in boarding_passes]

# define a function to compute the seat ID
compute_seat_ID = lambda row, column: 8 * row + column

# compute the seat ID's
seat_IDs = [compute_seat_ID(*seat) for seat in seats]

print(f'The highest seat ID on a boarding pass is: {max(seat_IDs)}')

# part two
print('--- Part Two ---')
# compute the missing seats and their IDs
missing_seats = sorted(set(product(ROWS, COLUMNS)) - set(seats))
missing_seat_IDs = [compute_seat_ID(*seat) for seat in missing_seats]

# get the seat ID of my seat
for seat_ID in missing_seat_IDs:
    if seat_ID - 1 in seat_IDs and seat_ID + 1 in seat_IDs:
        my_seat_ID = seat_ID
        break  # early stopping condition
else:  # early stopping condition not reached
    print('Could not find the ID oy my seat')

print(f'The ID of my seat is: {my_seat_ID}')
