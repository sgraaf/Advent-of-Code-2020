#!/usr/bin/env python
# coding: utf-8
from collections import Counter, defaultdict

print('--- Day 21: Allergen Assessment ---')

# read the input data from `input.txt`
ingredients_counter = Counter()
allergen_to_ingredients = defaultdict(list)
with open('input.txt', 'r') as f:
    for line in f:
        line = line.rstrip(')\n')
        ingredients, allergens = line.split(' (contains ')
        ingredients = set(ingredients.split(' '))
        ingredients_counter.update(ingredients)  # update the counter
        for allergen in allergens.split(', '):
            allergen_to_ingredients[allergen].append(ingredients)


# part one
print('--- Part One ---')
# for each allergen, get the possible set of ingredients
allergen_to_ingredients = {allergen: set.intersection(
    *ingredients) for allergen, ingredients in allergen_to_ingredients.items()}
# compute the possibly allergenic ingredients (and non-allergenic ingredients)
allergenic_ingredients = set.union(*allergen_to_ingredients.values())
non_allergenic_ingredients = set(ingredients_counter.keys()) - allergenic_ingredients
# compute the number of times the non-allergenic ingredients appear
non_allergenic_count = sum(ingredients_counter[ingredient] for ingredient in non_allergenic_ingredients)
print(f'The number of times an ingredient appears that can\'t possibly contain any allergens is: {non_allergenic_count}')

# part two
print('--- Part Two ---')
# determine which allergen is contained by which ingredient
allergen_to_ingredient = {}
while len(allergen_to_ingredient) != len(allergen_to_ingredients):
    for allergen, ingredients in allergen_to_ingredients.items():
        if len(ingredients) == 1:  # only one possible ingredient
            ingredient = ingredients.pop()
            allergen_to_ingredient[allergen] = ingredient
            # remove the ingredient from other ingredient lists
            for _ingredients in allergen_to_ingredients.values():
                if ingredient in _ingredients:
                    _ingredients.remove(ingredient)
# get the dangerous ingredients into a list
dangerous_ingredient_list = [ingredient for _, ingredient in sorted(allergen_to_ingredient.items())]
print(f'My canonical dangerous ingredient list is: {",".join(dangerous_ingredient_list)}')
