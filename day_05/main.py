from input import Input
from ingredients import Ingredients

input = Input('day_05/input.txt')
ingredients = Ingredients(input.id_ranges)

fresh_ingredients = 0

for id in input.get_ids():
	if ingredients.is_fresh(id):
		fresh_ingredients += 1

print(f'Number of fresh ingredients: {fresh_ingredients}')