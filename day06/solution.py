#!/usr/bin/env python
# coding: utf-8

print('--- Day 6: Custom Customs ---')

# read the input data from `input.txt` into a list `answers`
answers = []
with open('input.txt', 'r') as f:
    answer = []  # initialize an empty answer list
    for line in f:
        line = line.rstrip('\n')
        if line == '':  # blank line, end of group answer
            answers.append(answer)
            answer = []  # reset the answer set
        else:
            answer.append(set(line))
    else:  # final answer
        answers.append(answer)

# part one
print('--- Part One ---') 
sum_answer_count_1 = sum([len(set.union(*answer)) for answer in answers])
print(f'The sum of the answer counts is: {sum_answer_count_1}')

# part two
print('--- Part Two ---')
sum_answer_count_2 = sum([len(set.intersection(*answer)) for answer in answers])
print(f'The sum of the answer counts is: {sum_answer_count_2}')
