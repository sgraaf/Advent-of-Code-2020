#!/usr/bin/env python
# coding: utf-8
from copy import deepcopy
from typing import List, Optional

print('--- Day 23: Crab Cups ---')

# read the input data from `input.txt` into two lists `player_1_cards` and `player_2_cards`
cups = [6, 5, 3, 4, 2, 7, 9, 1, 8]
_cups = deepcopy(cups)
# cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]


# part one
print('--- Part One ---')
# define a function to simulate a move of crab cups
def move(cups: List[int], previous_cup: Optional[int] = None) -> List[int]:
    # get the current cup
    current_cup = cups[(cups.index(previous_cup) + 1) % len(cups)] if previous_cup else cups[0]
    cc_idx = cups.index(current_cup)
    # pick up the three cups clockwise from the current cup
    cups_picked_up = [cups[idx % len(cups)] for idx in range(cc_idx+1, cc_idx+4)]
    cups = [cup for cup in cups if cup not in cups_picked_up]
    # get the destination cup
    destination_cup = current_cup - 1
    while destination_cup in cups_picked_up or destination_cup < min(cups):
        destination_cup -= 1
        if destination_cup < min(cups):
            destination_cup = max(cups)
    dc_idx = cups.index(destination_cup)
    # place the picked up cups directly clockwise from the destination cup
    cups = cups[:dc_idx+1] + cups_picked_up + cups[dc_idx+1:]
    return current_cup, cups
# simulate 100 moves    
previous_cup = None
for _ in range(100):
    previous_cup, cups = move(cups, previous_cup)
# get the labels on the cups after cup 1
print(f'The labels on the cups after cup 1 are: {"".join(map(str, cups[cups.index(1)+1:] + cups[:cups.index(1)]))}')


# part two
print('--- Part Two ---')
# extend our cups to 1M
cups = _cups + list(range(max(cups) + 1, 1_000_000+1))
# simulate 10M moves    
previous_cup = None
for _ in range(10_000_000):
    previous_cup, cups = move(cups, previous_cup)
