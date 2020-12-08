#!/usr/bin/env python
# coding: utf-8
import re
from copy import deepcopy
from typing import List, Tuple

print('--- Day 8: Handheld Halting ---')

# read the input data from `input.txt` into a list `instructions`
instructions = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        # get the operation and argument
        operation, argument = re.match(r'(\w{3}) \+?(-?\d+)', line).groups()
        # add the operation and argument to the instructions list
        instructions.append((operation, int(argument)))

# define a function to run the program instructions
def run_instructions(instructions: List[Tuple[str, int]]) -> int:
    instructions_run = set()  # set of already run instructions (to make sure we don't execute an instruction a second time)
    acc = 0  # accumulator
    pointer = 0  # instruction pointer
    while pointer not in instructions_run:
        if pointer == len(instructions):  # no infinite loop
            break
        instructions_run.add(pointer)  # add the pointer to the set of already run instructions
        operator, argument = instructions[pointer]  # unpack instruction
        if operator == 'acc':  # accumulation
            acc += argument
            pointer += 1
        elif operator == 'jmp':  # jump
            pointer += argument
        elif operator == 'nop':  # no operation
            pointer += 1
    else:  # infinite loop
        return acc, False
    return acc, True  # no infinite loop

# part one
print('--- Part One ---')
print(f'The value of the accumulator is: {run_instructions(instructions)[0]}')

# part two
print('--- Part Two ---')
# define a function to "flip" the operation
flip_operation = lambda operation: 'jmp' if operation == 'nop' else 'nop'
# get a list of pointers and operations to change
pointers_operations_to_change = [(i, flip_operation(operation)) for i, (operation, _) in enumerate(instructions) if operation in {'jmp', 'nop'}]

for pointer, operation in pointers_operations_to_change:
    instructions_changed = deepcopy(instructions)  # create a copy of the instructions
    instructions_changed[pointer] = operation, instructions_changed[pointer][1]  # change the operation
    acc, is_terminated = run_instructions(instructions_changed)
    if is_terminated:  # program termination, no infinite loop
        break
else:
    print('Could not find an operation change that would cause the program to terminate.')
print(f'The value of the accumulator after the program terminates is: {acc}')
