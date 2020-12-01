#!/usr/bin/env python
# coding: utf-8
from itertools import product

# read the input data from `input.txt` into a list `l`
l = list(map(int, open('input.txt', 'r').readlines()))

# part one
print('--- Part One ---')
for i, j in product(l, l):
    if i + j == 2020:
        print(f'{i} + {j} = 2020')
        print(f'{i} * {j} = {i * j}')
        break  # early stopping condition
else:  # early stopping condition not reached
    print('Could not find two entries that sum to 2020')

# part two
print('--- Part Two ---')
for i, j, k in product(l, l, l):
    if i + j + k == 2020:
        print(f'{i} + {j} + {k} = 2020')
        print(f'{i} * {j} * {k} = {i * j * k}')
        break  # early stopping condition
else:  # early stopping condition not reached
    print('Could not find three entries that sum to 2020')
