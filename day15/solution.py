#!/usr/bin/env python
# coding: utf-8

print('--- Day 15: Rambunctious Recitation ---')

# read the input data from `input.txt` into a list `numbers`
numbers = [2, 0, 6, 12, 1, 3]

# part one
print('--- Part One ---')
# use `list.count()` and `list.index()`
while len(numbers) < 2020:
    last_number = numbers[-1]
    if numbers.count(last_number) == 1:  # first time
        numbers.append(0)
    else:
        numbers.append(numbers[:-1][::-1].index(last_number) + 1)
print(f'Given my starting numbers, the 2020th number spoken is: {numbers[-1]}')

# part two
print('--- Part Two ---')
# use a `dict` for higher performance
last_number = numbers[-1]
numbers = numbers[:-1]
number_to_idx = {number: idx for idx, number in enumerate(numbers)}
for idx in range(len(numbers), 30000000 - 1):
    if last_number not in number_to_idx:  # first time
        next_number = 0
    else:
        next_number = idx - number_to_idx[last_number]
    number_to_idx[last_number] = idx
    last_number = next_number
print(f'Given my starting numbers, the 30000000th number spoken is: {last_number}')
