#!/usr/bin/env python
# coding: utf-8
import re

print('--- Day 2: Password Philosophy ---')

# read the input data from `input.txt` into a list `l`
l = []
with open('input.txt', 'r') as f:
    for line in f:
        # extract the relevant data using regex
        m = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line.rstrip('\n'))
        low = int(m.group(1))
        high = int(m.group(2))
        letter = m.group(3)
        password = m.group(4)
        l.append((low, high, letter, password))

# part one
print('--- Part One ---')
num_valid_passwords_1 = sum([low <= len(re.findall(letter, password)) <= high for low, high, letter, password in l])
print(f'Number of valid passwords: {num_valid_passwords_1}')

# part two
print('--- Part Two ---')
num_valid_passwords_2 = sum([(password[low-1] == letter) ^ (password[high-1] == letter) for low, high, letter, password in l])  # uses bitwise XOR
print(f'Number of valid passwords: {num_valid_passwords_2}')
