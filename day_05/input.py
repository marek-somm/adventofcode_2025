
class Input:

	def __init__(self, filepath: str):
		self.id_ranges, self.ids = self.read_lines(filepath)

	
	def read_lines(self, filepath: str) -> tuple[list[str], list[str]]:
		with open(filepath, 'r') as file:
			content = file.read().strip().split('\n\n')
			ranges = [line.strip() for line in content[0].split('\n')]
			ids = [line.strip() for line in content[1].split('\n')]
			return ranges, ids
		

	def get_id_ranges(self) -> list[str]:
		return self.id_ranges
	

	def get_ids(self) -> list[int]:
		return [int(id) for id in self.ids]