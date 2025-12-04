
class Input:

	def __init__(self, filepath: str):
		self.lines = self.read_lines(filepath)

	
	def read_lines(self, filepath: str) -> list[str]:
		with open(filepath, 'r') as file:
			return [line.strip() for line in file.readlines()]
		
	
	def get_lines(self) -> list[str]:
		return self.lines
