#!/usr/bin/env python
# coding: utf-8
from copy import deepcopy
from typing import Dict, List, Optional
from tqdm import trange, tqdm

print('--- Day 23: Crab Cups ---')

# read the input data from `input.txt` into a list `cups`
cups = [6, 5, 3, 4, 2, 7, 9, 1, 8]
_cups = deepcopy(cups)

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

def move_cups(cups: List[int], N: Optional[int] = 100) -> Dict[int, Node]:
    min_cups = min(cups)
    max_cups = max(cups)
    nodes = {cup: Node(cup) for cup in cups}

    for cup, next_cup in zip(cups, cups[1:] + cups[:1]):
        nodes[cup].next = nodes[next_cup]

    current_node = nodes[cups[0]]
    # simulate N moves
    for _ in trange(N):
        a = current_node.next
        b = a.next
        c = b.next

        destination_cup = current_node.val - 1
        while destination_cup in {a.val, b.val, c.val} or destination_cup < min_cups:
            destination_cup -= 1
            if destination_cup < min_cups:
                destination_cup = max_cups
        destination_node = nodes[destination_cup]

        current_node.next = c.next
        current_node = c.next
        c.next = destination_node.next
        destination_node.next = a

    return nodes


# part one
print('--- Part One ---')
# simulate 100 moves    
nodes = move_cups(cups, 100)

# get the cups in the order destination_node moving
cups_destination_node = []
current_node = nodes[1]
while len(cups_destination_node) < len(cups):
    cups_destination_node.append(current_node.val)
    current_node = current_node.next

# get the labels on the cups destination_node cup 1
print(f'The labels on the cups destination_node cup 1 are: {"".join(map(str, cups_destination_node[cups_destination_node.index(1)+1:] + cups_destination_node[:cups_destination_node.index(1)]))}')


# part two
print('--- Part Two ---')
# extend our `cups` list through 1M
cups = _cups + list(range(max(_cups) + 1, 1_000_000 + 1))

# simulate 10M moves  
nodes = move_cups(cups, 10_000_000)

# get the labels on the cups destination_node cup 1
print(f'If you multiply the labels together of the two cups that end up immediately clockwise of cup 1, you get: {nodes[1].next.val * nodes[1].next.next.val}')
