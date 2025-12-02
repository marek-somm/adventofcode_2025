

class Dial:
	min_value: int = 0
	max_value: int = 99

	current_value: int


	def __init__(self, starting_value: int = 0) -> None:
		self.current_value = starting_value

	
	def turn(self, value: int) -> None:
		self.current_value = self.min_value + ((self.current_value - self.min_value + value) % (self.max_value - self.min_value + 1))
	

	def is_zero(self) -> bool:
		return self.current_value == 0
	

	def print(self) -> None:
		print(f"Dial value: {self.current_value}")
