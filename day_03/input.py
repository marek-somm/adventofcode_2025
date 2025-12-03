
class Input:

	def __init__(self, filepath: str):
		self.battery_banks = self.read_battery_banks(filepath)

	
	def read_battery_banks(self, filepath: str) -> list[str]:
		with open(filepath, 'r') as file:
			return [line.strip() for line in file.readlines()]
	

	def find_maximum_two_batteries(self, battery_bank: str) -> tuple[int, int]:
		max1 = max2 = 0

		for joltage_string in battery_bank[:-1]:
			joltage = int(joltage_string)
			if joltage > max1:
				max2 = 0
				max1 = joltage
			elif joltage > max2:
				max2 = joltage

		last_joltage = int(battery_bank[-1])
		if max2 < last_joltage:
			max2 = last_joltage

		return max1, max2
	

	def find_maximum_n_batteries(self, battery_bank: str, n: int) -> list[int]:
		max_joltage = []
		left_bound = 0

		battery_bank_len = len(battery_bank)
		for i in range(n):
			right_bound = battery_bank_len-(n-1-i)
			max, max_index = self.find_maximum_battery(battery_bank[left_bound:right_bound])
			max_joltage.append(max)
			left_bound += max_index + 1

		return max_joltage
	

	def find_maximum_battery(self, battery_bank: str) -> tuple[int, int]:
		max_battery = 0
		max_index = 0

		for index, joltage_string in enumerate(battery_bank):
			joltage = int(joltage_string)
			if joltage > max_battery:
				max_battery = joltage
				max_index = index

		return max_battery, max_index
	

	def get_battery_banks(self) -> list[str]:
		return self.battery_banks