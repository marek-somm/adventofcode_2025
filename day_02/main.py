from input import Input

input = Input('day_02/input.txt')
ids = input.get_ids()

invalid_id_sum = 0

for id in ids:
	if not input.is_valid_id(id):
		invalid_id_sum += id

print(f'Sum of all invalid IDs: {invalid_id_sum}')