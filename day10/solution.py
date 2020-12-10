#!/usr/bin/env python
# coding: utf-8
from typing import Any, List

print('--- Day 10: Adapter Array ---')

REPEAT_BASES = {2: 2, 3: 4, 4: 7}  # bases for exponentation

# read the input data from `input.txt` into a list `joltages`
joltages = [0] + sorted(map(int, open('input.txt', 'r').readlines()))

# part one
print('--- Part One ---')
joltage_differences = [joltages[i] - joltages[i-1] for i in range(1, len(joltages))]
print(f'The number of 1-jolt differences multiplied by the number of 3-jolt differences is: {joltage_differences.count(1) * (joltage_differences.count(3) + 1)}')

# part two
print('--- Part Two ---')
# define functions to find the max number of subsequent repeats of a value in a list
count_sublist_occurrence = lambda s, l: sum(l[i:i+len(s)] == s for i in range(len(l)))
def find_max_repeat(l: List, val: Any) -> int:
    repeat = 1
    while count_sublist_occurrence([val] * repeat, l) >= 1:
        repeat += 1
    else:
        return repeat - 1

# compute the number of arrangements
num_arrangements = 1
for repeat in range(find_max_repeat(joltage_differences[1:], 1), 1, -1):  # go from largest repeat to smallest
    repeat_count = 0
    for i in range(len(joltage_differences)-repeat, -1, -1):  # iterate through the list backwards (because of deletes)
        if joltage_differences[i:i+repeat] == [1] * repeat:
            repeat_count += 1
            del joltage_differences[i:i+repeat]
    num_arrangements *= REPEAT_BASES[repeat]**repeat_count

print(f'The total number of distinct ways I can arrange the adapters to connect the charging outlet to my device is: {num_arrangements}')
