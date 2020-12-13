#!/usr/bin/env python
# coding: utf-8
from functools import reduce
from operator import mul
from typing import List

print('--- Day 13: Shuttle Search ---')

# define a function to compute the Chinese Remainder Theorem (CRT)
def crt(modulos: List[int], remainders: List[int]) -> int:
    N = reduce(mul, modulos)
    t = sum(r * N//m * pow(N//m, m-2, m) for m, r in zip(modulos, remainders))
    return t % N

with open('input.txt', 'r') as f:
    earliest_depart = int(f.readline().rstrip('\n'))
    buses = [(delay, int(bus_ID)) for delay, bus_ID in enumerate(f.readline().rstrip('\n').split(',')) if bus_ID != 'x']
    bus_IDs = [bus_ID for _, bus_ID in buses]
    remainders = [(bus_ID - delay) % bus_ID for delay, bus_ID in buses]  # remainders for CRT

# part one
print('--- Part One ---')
compute_wait_time = lambda bus_ID: bus_ID * (earliest_depart // bus_ID + 1) - earliest_depart
earliest_bus_ID = min(bus_IDs, key=compute_wait_time)
print(f'The ID of the earliest bus I can take multiplied by the number of minutes I\'ll need to wait for is: {earliest_bus_ID * compute_wait_time(earliest_bus_ID)}')

# part two
print('--- Part Two ---')
earliest_timestamp = crt(bus_IDs, remainders)
print(f'The earliest timestamp that all of the buses depart at offsets matching their positions is: {earliest_timestamp}')
