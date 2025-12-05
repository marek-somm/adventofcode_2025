from input import Input
from ingredients import Ingredients

input = Input('day_05/input.txt')
ingredients = Ingredients(input.id_ranges)

id_ranges_count = ingredients.get_ranges_count()

total_fresh_ids = 0

for id_range_count in id_ranges_count:
	total_fresh_ids += id_range_count

print(f"Total fresh ingredient IDs: {total_fresh_ids}")