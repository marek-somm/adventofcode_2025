
class Ingredients:
	def __init__(self, id_ranges: list[str]):
		self.id_ranges = self.convert_ranges(id_ranges)

	
	def convert_ranges(self, id_ranges: list[str]) -> list[tuple[int, int]]:
		return [(int(id_range.split("-")[0]), int(id_range.split("-")[1])) for id_range in id_ranges]
	

	def is_fresh(self, id: int) -> bool:
		for start, end in self.id_ranges:
			if start <= id <= end:
				return True
		return False