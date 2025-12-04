from input import Input
from grid import Grid

input = Input('day_04/input.txt')
grid = Grid(input.get_lines())

total_roll_count = 0

for x in range(grid.get_width()):
	for y in range(grid.get_height()):
		value = grid.get_value_at(x, y)
		if value == 1:
			surrounding = grid.count_surrounding(x, y)
			if surrounding < 4:
				total_roll_count += 1

print(f'Total roll count: {total_roll_count}')