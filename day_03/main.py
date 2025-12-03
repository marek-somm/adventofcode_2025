from input import Input

input = Input('day_03/input.txt')
battery_banks = input.get_battery_banks()

n = 12
total_joltage = 0

for battery_bank in battery_banks:
	max_batteries = input.find_maximum_n_batteries(battery_bank, n)
	maximum_joltage = "".join(str(battery) for battery in max_batteries)

	total_joltage += int(maximum_joltage)

print(f'Total joltage: {total_joltage}')
