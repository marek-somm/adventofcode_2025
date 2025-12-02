

class Input:

	def __init__(self, filename: str) -> None:
		with open(filename, 'r') as file:
			self.lines = [line.strip() for line in file.readlines()]


	def get_next(self) -> int:
		if len(self.lines) == 0:
			return 0
		
		return self.convert_to_int(self.lines.pop(0))
	

	def convert_to_int(self, value: str) -> int:
		return int(value.replace("L","-").replace("R",""))
	

	def has_more(self) -> bool:
		return len(self.lines) > 0