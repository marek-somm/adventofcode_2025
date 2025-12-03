from input import Input

input = Input('day_03/input.txt')
battery_banks = input.get_battery_banks()

total_joltage = 0

for battery_bank in battery_banks:
	max1, max2 = input.find_maximum_two_batteries(battery_bank)
	maximum_joltage = int(str(max1) + str(max2))

	total_joltage += maximum_joltage

print(f'Total joltage: {total_joltage}')
