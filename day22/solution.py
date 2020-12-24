#!/usr/bin/env python
# coding: utf-8
from copy import deepcopy
from typing import List, Tuple

print('--- Day 22: Crab Combat ---')

# read the input data from `input.txt` into two lists `player_1_cards` and `player_2_cards`
player_1_cards, player_2_cards = open('input.txt', 'r').read().rstrip('\n').split('\n\n')
# convert numbers to int
player_1_cards = list(map(int, player_1_cards.split('\n')[1:]))
player_2_cards = list(map(int, player_2_cards.split('\n')[1:]))


# part one
print('--- Part One ---')
# define a function to play a game of Combat
def Combat(cards_1: List[int], cards_2: List[int]) -> Tuple[bool, List[int]]:
    while cards_1 and cards_2:  # no empty deck
        # draw the top card
        card_1 = cards_1.pop(0)
        card_2 = cards_2.pop(0)
        # compare cards
        if card_1 > card_2:
            # add the cards to the bottom of the deck
            cards_1 += [card_1, card_2]
        elif card_2 > card_1:
            # add the cards to the bottom of the deck
            cards_2 += [card_2, card_1]
    return (True, cards_1) if cards_1 else (False, cards_2)
# play the game of Combat
_, winning_cards = Combat(deepcopy(player_1_cards), deepcopy(player_2_cards))
# compute the score
score = sum(card * (i + 1) for i, card in enumerate(reversed(winning_cards)))
print(f'The winning player\'s score is: {score}')


# part two
print('--- Part Two ---')
# define a function to play a game of Recursive Combat
def RecursiveCombat(cards_1: List[int], cards_2: List[int]) -> Tuple[bool, List[int]]:
    rounds = set()
    while cards_1 and cards_2:  # no empty deck
        round_key = (tuple(cards_1), tuple(cards_2))
        if round_key in rounds:  # game instantly ends, player 1 wins
            return (True, cards_1)
        # add the cards of the current round to the set
        rounds.add(round_key)
        # draw the top card
        card_1 = cards_1.pop(0)
        card_2 = cards_2.pop(0)
        # get the winner
        if len(cards_1) >= card_1 and len(cards_2) >= card_2:  # sub-game
            winner, _ = RecursiveCombat(
                deepcopy(cards_1)[:card_1], deepcopy(cards_2)[:card_2])
        else:  # compare cards
            winner = card_1 > card_2
        # add the cards to the bottom of the deck
        if winner:
            cards_1 += [card_1, card_2]
        else:
            cards_2 += [card_2, card_1]
    return (True, cards_1) if cards_1 else (False, cards_2)
# play the game of Recursive Combat
_, winning_cards = RecursiveCombat(deepcopy(player_1_cards), deepcopy(player_2_cards))
# compute the score
score = sum(card * (i + 1) for i, card in enumerate(reversed(winning_cards)))
print(f'The winning player\'s score is: {score}')
