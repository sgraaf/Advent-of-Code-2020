#!/usr/bin/env python
# coding: utf-8
from itertools import count
from typing import Optional

print('--- Day 25: Combo Breaker ---')


# read the input data from `input.txt` into two `*_public_key`s
with open('input.txt', 'r') as f:
    card_public_key = int(f.readline().rstrip('\n'))
    door_public_key = int(f.readline().rstrip('\n'))


# part one
print('--- Part One ---')
# define a function to transform the subject number
def transform_subject_number(subject_number: int, public_key: Optional[int] = None, loop_size: Optional[int] = None) -> int:
    value = 1
    for i in count(1):
        value *= subject_number
        value %= 20201227
        if public_key:
            if value == public_key:
                return i
        elif loop_size:
            if i == loop_size:
                return value
        else:
            raise ValueError(
                'At least one of `public_key` or `loop_size` should be specified.')
# compute the loop size for both the card and door
card_loop_size = transform_subject_number(7, public_key=card_public_key)
door_loop_size = transform_subject_number(7, public_key=door_public_key)
# compute the encryption key
encryption_key_1 = transform_subject_number(card_public_key, loop_size=door_loop_size)
encryption_key_2 = transform_subject_number(door_public_key, loop_size=card_loop_size)
assert encryption_key_1 == encryption_key_2  # make sure both encryption keys are equal
print(f'The encryption key that the handshake is trying to establish is: {encryption_key_1}')
