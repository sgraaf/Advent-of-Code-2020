#!/usr/bin/env python
# coding: utf-8
import re
from typing import Any

print('--- Day 4: Passport Processing ---')

# required fields (and corresponding data types)
REQUIRED_FIELDS = (
    'byr',  # Birth Year
    'iyr',  # Issue Year
    'eyr',  # Expiration Year
    'hgt',  # Height
    'hcl',  # Hair Color
    'ecl',  # Eye Color
    'pid',  # Passport ID
    'cid',  # Country ID
)

# read the input data from `input.txt` into a list `passports`
passports = []
with open('input.txt', 'r') as f:
    passport = {}  # initialize an empty passport dict
    for line in f:
        line = line.rstrip('\n')
        if line == '':  # blank line, end of passport
            passports.append(passport)
            passport = {}  # reset the passport dict
        else:
            for required_field in REQUIRED_FIELDS:
                match = re.search(f'{required_field}:([#a-z0-9]+)', line)
                if match:
                    passport[required_field] = match.group(1)
    else:  # final passport
        passports.append(passport)

# part one
print('--- Part One ---') 
num_valid_passports_1 = sum([set(REQUIRED_FIELDS) - set([*passport]) <= {'cid'} for passport in passports])  # uses set operations
print(f'The number of valid passports is: {num_valid_passports_1}')

# part two
print('--- Part Two ---')
# define some validation functions
is_four_digits = lambda val: bool(re.match(r'\d{4}', val))
is_in_range = lambda val, low, high: low <= int(val) <= high
is_valid_byr = lambda val: is_in_range(val, 1920, 2002) if is_four_digits(val) else False
is_valid_iyr = lambda val: is_in_range(val, 2010, 2020) if is_four_digits(val) else False
is_valid_eyr = lambda val: is_in_range(val, 2020, 2030) if is_four_digits(val) else False
def is_valid_hgt(val: Any) -> bool:
    match = re.match(r'(\d+)(cm|in)', val)
    if match:
        if match.group(2) == 'cm':
            return 150 <= int(match.group(1)) <= 193
        elif match.group(2) == 'in':
            return 59 <= int(match.group(1)) <= 76
        return False
    return False
is_valid_hcl = lambda val: bool(re.match(r'#[a-f0-9]{6}', val))
is_valid_ecl = lambda val: val in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
is_valid_pid = lambda val: bool(re.fullmatch(r'\d{9}', val))

# count the number of valid passports
num_valid_passports_2 = 0
for passport in passports:
    if set(REQUIRED_FIELDS) - set([*passport]) <= {'cid'}:  # all required fields present w/ cid ignored
        if (
            is_valid_byr(passport['byr']) &
            is_valid_iyr(passport['iyr']) & 
            is_valid_eyr(passport['eyr']) &
            is_valid_hgt(passport['hgt']) &
            is_valid_hcl(passport['hcl']) &
            is_valid_ecl(passport['ecl']) &
            is_valid_pid(passport['pid'])
        ):  # all values are valid
            num_valid_passports_2 += 1
print(f'The number of valid passports is: {num_valid_passports_2}')