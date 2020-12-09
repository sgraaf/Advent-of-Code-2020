#!/usr/bin/env python
# coding: utf-8
from itertools import count

print('--- Day 9: Encoding Error ---')

# read the input data from `input.txt` into a list `numbers`
numbers = list(map(int, open('input.txt', 'r').readlines()))

# part one
print('--- Part One ---')
for i, n in enumerate(numbers):
    if i >= 25:  # past the preamble
        window = numbers[i-25:i]
        for j, m in enumerate(window):
            if n - m in window:
                break
        else:
            invalid_number = n
            print(f'The first number that is not the sum of two of the 25 numbers before it is: {invalid_number}')
            break

# part two
print('--- Part Two ---')
for n in count(2):  # sliding window size
    for i in range(n-1, len(numbers)):
        window = numbers[i-n:i]
        if sum(window) == invalid_number:  # contiguous set that sums to the invalid number
            encryption_weakness = min(window) + max(window)
            print(f'The encryption weakness in my XMAS-encrypted list of numbers is: {encryption_weakness}')
            break
    else:
        continue
    break
