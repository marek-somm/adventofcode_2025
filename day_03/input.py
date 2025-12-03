
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
	

	def get_battery_banks(self) -> list[str]:
		return self.battery_banks