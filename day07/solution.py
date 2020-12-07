#!/usr/bin/env python
# coding: utf-8
import re
from typing import Optional, Set

print('--- Day 7: Handy Haversacks ---')

# our specific bag type
BAG_TYPE = 'shiny gold'

# read the input data from `input.txt` into a dict `rules` (basic weighted digraph)
rules = {}
with open('input.txt', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        # get the bag type and the bag types (and their counts) it contains
        container = re.match(r'([a-z\s]+) bag', line).group(1)
        contains = re.findall('(\d) ([a-z\s]+) bag', line)
        # add the rule to the rules dict
        rules[container] = {bag_type: int(count) for count, bag_type in contains}

# part one
print('--- Part One ---')
# global variable to maintain a set of all containers (already seen)
all_containers = set()

def count_containers(bag_type: str) -> int:
    global all_containers
    containers = {k for k, v in rules.items() if bag_type in v.keys()} - all_containers
    if len(containers) == 0:  # `bag_type` is not contained by any other bag
        return 0
    all_containers |= containers  # update all containers
    return len(containers) + sum(count_containers(bag_type) for bag_type in containers)

print(f'The number of bag colors that can eventually contain at least one shiny gold bag is: {count_containers(BAG_TYPE)}')

# part two
print('--- Part Two ---')
def count_contains(bag_type: str) -> int:
    if bag_type not in rules:  # `bag_type` contains 0 other bags
        return 1
    return 1 + sum(count * count_contains(bag_type) for bag_type, count in rules[bag_type].items())

print(f'The number of individual bags that are required inside my single shiny gold bag is: {count_contains(BAG_TYPE)-1}')
