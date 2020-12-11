#!/usr/bin/env python
# coding: utf-8
from copy import deepcopy
from typing import List, Optional

print('--- Day 11: Seating System ---')

# read the input data from `input.txt` into a list `seats_grid`
seats_grid = [list(line.rstrip('\n')) for line in open('input.txt', 'r')]
_seats_grid = deepcopy(seats_grid)


def reset_grid():
    return _seats_grid


def find_adjacent_seats(grid: List[List[str]], i: int, j: int, see_first_seat: Optional[bool] = False) -> List[str]:
    adjacent_seats = []
    for di, dj in [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]:
        if 0 <= i + di <= len(grid) - 1 and 0 <= j + dj <= len(grid[0]) - 1:
            seat = grid[i + di][j + dj]
            if see_first_seat:
                factor = 2
                while seat == '.':  # floor
                    if 0 <= i + factor * di <= len(grid) - 1 and 0 <= j + factor * dj <= len(grid[0]) - 1:
                        seat = grid[i + factor * di][j + factor * dj]
                        factor += 1
                    else:
                        break
                else:
                    adjacent_seats.append(seat)
            else:
                adjacent_seats.append(seat)
    return adjacent_seats


def update_grid(grid: List[List[str]], occupied_seat_threshold: Optional[int] = 4) -> List[List[str]]:
    out_grid = deepcopy(grid)
    for i, row in enumerate(seats_grid):
        for j, seat in enumerate(row):
            adjacent_seats = find_adjacent_seats(seats_grid, i, j, see_first_seat=occupied_seat_threshold == 5)
            if seat == 'L':  # empty seat
                if '#' not in adjacent_seats:
                    out_grid[i][j] = '#'  # update seat to occupied
            elif seat == '#':  # occupied seat
                if adjacent_seats.count('#') >= occupied_seat_threshold:
                    out_grid[i][j] = 'L'  # update seat to empty
    return out_grid


# part one
print('--- Part One ---')
# apply the rules until no seats change state
previous_seats_grid = []
while seats_grid != previous_seats_grid:
    previous_seats_grid = seats_grid
    seats_grid = update_grid(seats_grid)
print(f'The number of seats that end up occupied is: {sum(sum(seat == "#" for seat in row) for row in seats_grid)}')

# part two
print('--- Part Two ---')
# reset the seats grid
seats_grid = reset_grid()

# apply the rules until no seats change state
previous_seats_grid = []
while seats_grid != previous_seats_grid:
    previous_seats_grid = seats_grid
    seats_grid = update_grid(seats_grid, occupied_seat_threshold=5)
print(f'The number of seats that end up occupied is: {sum(sum(seat == "#" for seat in row) for row in seats_grid)}')
