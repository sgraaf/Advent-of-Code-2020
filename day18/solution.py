#!/usr/bin/env python
# coding: utf-8
from copy import deepcopy
from typing import List, Tuple, Union

print('--- Day 18: Operation Order ---')


# define a function to parse an expression (from string to list)
def parse_expression(expression: str) -> List[Union[int, str]]:
    expression = list(expression.replace(' ', ''))
    for idx, c in enumerate(expression):
        if c not in {'(', ')', '+', '*'}:
            expression[idx] = int(c)
    return expression


# define a function to find the (nested) parentheses in an expression (sorted left-to-right from inner to outer)
def find_parentheses(expression: Union[str, List[Union[int, str]]]) -> List[Tuple[int, int]]:
    parentheses_stack = []
    parentheses_locations = []
    for idx, c in enumerate(expression):
        if c == '(':
            parentheses_stack.append(idx)
        elif c == ')':
            parentheses_locations.append((parentheses_stack.pop(), idx))
    return parentheses_locations


# define a function to find the outermost parantheses in an expression
def find_outermost_parentheses(expression: Union[str, List[Union[int, str]]]) -> List[Tuple[int, int]]:
    if (parentheses_locations := find_parentheses(expression)):
        outermost_parentheses_locations = []
        starts, ends = zip(*parentheses_locations)
        for idx, (start, end) in enumerate(zip(starts, ends)):
            if not any(starts[jdx] <= start and ends[jdx] >= end for jdx in range(idx + 1, len(starts))):
                outermost_parentheses_locations.append((start, end))
        return outermost_parentheses_locations
    return []


# read the input data from `input.txt` into list `expressions`
expressions = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        expressions.append(parse_expression(line))
_expressions = deepcopy(expressions)

# part one
print('--- Part One ---')
# define a function to (recursively) solve an expression
def solve_expression_1(expression: List[Union[int, str]]) -> int:
    if (parentheses_locations := find_outermost_parentheses(expression)):  # resolve parentheses
        for start, end in reversed(parentheses_locations):
            expression[start:end+1] = [solve_expression_1(expression[start+1:end])]

    # solve the expression left-to-right
    result = 0
    operator = '+'
    for c in expression:
        if c in {'+', '*'}:  # change in operator
            operator = c
        else:  # perform operation
            if operator == '+':
                result += c
            else:
                result *= c
    return result

print(f'The sum of the resulting values is: {sum(solve_expression_1(expression) for expression in expressions)}')

# part two
print('--- Part Two ---')
# (re-(define a function to (recursively) solve an expression
def solve_expression_2(expression: List[Union[int, str]]) -> int:
    # the expression contains parentheses
    if (parentheses_locations := find_outermost_parentheses(expression)):
        for start, end in reversed(parentheses_locations):
            expression[start:end+1] = [solve_expression_2(expression[start+1:end])]

    # resolve addition
    addition_idxs = [idx for idx, c in enumerate(expression) if c == '+']
    for addition_idx in reversed(addition_idxs):
        expression[addition_idx-1:addition_idx+2] = [expression[addition_idx-1] + expression[addition_idx+1]]

    # resolve multiplication
    result = 1
    for c in expression:
        if c != '*':
            result *= c
    return result

expressions = _expressions  # reset the expressions
print(f'The sum of the resulting values using these new rules is: {sum(solve_expression_2(expression) for expression in expressions)}')
