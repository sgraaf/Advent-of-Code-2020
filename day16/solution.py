#!/usr/bin/env python
# coding: utf-8
import re
from collections import defaultdict
from functools import reduce
from operator import mul

print('--- Day 16: Ticket Translation ---')

# read the input data from `input.txt` into a dict `rules`, a list `my_ticket` and a list `nearby_tickets`
rules = {}
my_ticket = []
nearby_tickets = []
with open('input.txt', 'r') as f:
    for _ in range(20):  # rules
        line = f.readline().rstrip('\n')
        rule = re.match(r'([\w\s]+):', line).group(1)
        ranges = [(int(low), int(high)) for low, high in re.findall(r'(\d+)\-(\d+)', line)]
        valid = {val for low, high in ranges for val in range(low, high + 1)}
        rules[rule] = valid
    
    next(f)  # skip empty line
    next(f)  # skip "your ticket:" line
    my_ticket = list(map(int, f.readline().rstrip('\n').split(',')))
    
    next(f)  # skip empty line
    next(f)  # skip "nearby tickets:" line
    for line in f:
         line = line.rstrip('\n')
         nearby_tickets.append(list(map(int, line.split(','))))

# part one
print('--- Part One ---')
# create a set of all possible valid values
all_valid = set.union(*rules.values())

# compute the error rate
error_rate = sum(sum(val for val in ticket if val not in all_valid) for ticket in nearby_tickets)
print(f'My ticket scanning error rate is: {error_rate}')

# part two
print('--- Part Two ---')
# discard invalid tickets
nearby_tickets = [ticket for ticket in nearby_tickets if all(val in all_valid for val in ticket)]

# for each field, get the ticket indices that could match it
field_to_idxs = defaultdict(list)
for field in rules:
    for idx in range(len(my_ticket)):
        all_values = [ticket[idx] for ticket in nearby_tickets]
        if all(val in rules[field] for val in all_values):
            field_to_idxs[field].append(idx)

# process of elimination
field_to_idx = {}
while max(len(idxs) for idxs in field_to_idxs.values()) > 1:
    for field, idxs in field_to_idxs.items():
        if len(idxs) == 1:
            idx = idxs[0]
            field_to_idx[field] = idx
            for _idxs in field_to_idxs.values():
                try:
                    _idxs.remove(idx)
                except ValueError:
                    pass

# compute the result
departure_mul = reduce(mul, [my_ticket[idx] for field, idx in field_to_idx.items() if field.startswith('departure')])
print(f'When I multiply the six fields from my ticket that start with the word departure, I get: {departure_mul}')
