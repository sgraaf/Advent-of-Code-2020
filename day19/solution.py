#!/usr/bin/env python
# coding: utf-8
import re
from typing import Dict, Optional

print('--- Day 19: Monster Messages ---')

# read the input data from `input.txt` into a dict `rules` and a list `messages`
rules = {}
messages = []
with open('input.txt', 'r') as f:
    while (line := f.readline().rstrip('\n')) != '':  # rules
        rule_number, rule = line.split(': ')
        rules[rule_number] = rule.replace('"', '')
    for line in f:  # messages
        line = line.rstrip('\n')
        messages.append(line)


def create_pattern(
    rules: Dict[str, str],
    rule_number: Optional[str] = '0',
    depth: Optional[int] = 0
) -> str:
    if depth >= 15:  # halt deep recursion
        return ''
    pattern = '('
    for c in rules[rule_number].split():
        if c.isdigit():  # rule number
            pattern += create_pattern(rules, c, depth+1)
        elif c == '|':  # or
            pattern += c
        else:  # terminal
            return c
    pattern += ')'
    return pattern

# part one
print('--- Part One ---')
# compile regex pattern
pattern = re.compile(create_pattern(rules))
# compute the number of valid messages
print(f'The number of messages that completely match rule 0 is: {sum(bool(pattern.fullmatch(message)) for message in messages)}')

# part two
print('--- Part Two ---')
# update rules
rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'
# compile regex pattern
pattern = re.compile(create_pattern(rules))
# compute the number of valid messages
print(f'The number of messages that completely match rule 0 is: {sum(bool(pattern.fullmatch(message)) for message in messages)}')
