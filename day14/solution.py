#!/usr/bin/env python
# coding: utf-8
import re
from collections import defaultdict

print('--- Day 14: Docking Data ---')

# define a function to set (or clear) a bit of a number
def set_bit(n: int, bit: int, val: int) -> int:
    mask = 1 << bit  # compute the mask
    n &= ~mask  # clear the bit
    if val:
        n |= mask  # set the bit
    return n


# read the input data from `input.txt` into a list `initialization_program`
initialization_program = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        if line.startswith('mask'):  # mask
            initialization_program.append(re.match(r'(\w{4}) = (\w{36})', line).groups() + (None,))
        elif line.startswith('mem'):  # mem
            action, address, value = re.match(r'(\w{3})\[(\d+)\] = (\d+)', line).groups()
            initialization_program.append((action, int(address), int(value)))

# part one
print('--- Part One ---')
# define a function to apply the mask to the value
def apply_mask_1(value: int, mask: str) -> int:
    for bit, val in enumerate(reversed(mask)):
        if val != 'X':
            value = set_bit(value, int(bit), int(val))
    return value


mem = defaultdict(int)  # initialize the memory space with 0's
mask = 'X' * 36  # initialize the mask
for instruction, *arguments in initialization_program:
    if instruction == 'mask':  # update the mask
        mask = arguments[0]
    elif instruction == 'mem':  # apply the mask and write the value to memory
        address, value = arguments
        mem[address] = apply_mask_1(value, mask)
print(f'The sum of all values left in memory after it completes is: {sum(mem.values())}')

# part two
print('--- Part Two ---')
# define a function to apply the mask to the address
def apply_mask_2(address: int, mask: str) -> int:
    address = list(f'{address:036b}')
    for bit, val in enumerate(mask):
        if val in {'1', 'X'}:
            address[int(bit)] = val
    return ''.join(address)


mem = defaultdict(int)  # reset the memory space with 0's
mask = 'X' * 36  # initialize the mask
for instruction, *arguments in initialization_program:
    if instruction == 'mask':  # update the mask
        mask = arguments[0]
    elif instruction == 'mem':
        address, value = arguments
        address = apply_mask_2(address, mask)  # apply the mask to the address
        num_floating = address.count('X')  # count the number of floating bits
        for i in range(2**num_floating):
            floating_replacements = f'{i:0{num_floating}b}'
            new_address = address
            for floating_replacement in floating_replacements:  # replace the floating bits
                new_address = new_address.replace('X', floating_replacement, 1)
            mem[int(new_address, 2)] = value  # write the value to memory
print(f'The sum of all values left in memory after it completes is: {sum(mem.values())}')
