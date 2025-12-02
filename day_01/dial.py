

class Dial:
	min_value: int = 0
	max_value: int = 99

	digit_count: int

	current_value: int


	def __init__(self, starting_value: int = 0) -> None:
		self.digit_count = self.max_value - self.min_value + 1
		self.current_value = starting_value

	
	def turn(self, value: int) -> None:
		self.current_value = self.min_value + ((self.current_value - self.min_value + value) % self.digit_count)
	

	def turn_and_count_zeros(self, value: int) -> int:
		old_value = self.current_value
		self.turn(value)

		sign = -1 if value < 0 else 1
		full_rotations = abs(value) // self.digit_count
		remainder = value - sign * self.digit_count * full_rotations
		return abs(full_rotations) + (1 if (old_value + remainder) > self.max_value or (old_value + remainder) <= self.min_value and old_value != 0 else 0)


	def is_zero(self) -> bool:
		return self.current_value == 0
	

	def print(self) -> None:
		print(f"Dial value: {self.current_value}")
