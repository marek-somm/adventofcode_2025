
class Ingredients:
	def __init__(self, id_ranges: list[str]):
		self.id_ranges = self.merge_ranges(self.convert_ranges(id_ranges))

	
	def convert_ranges(self, id_ranges: list[str]) -> list[tuple[int, int]]:
		return [(int(id_range.split("-")[0]), int(id_range.split("-")[1])) for id_range in id_ranges]
	

	def is_fresh(self, id: int) -> bool:
		for start, end in self.id_ranges:
			if start <= id <= end:
				return True
		return False
	

	def get_id_ranges(self) -> list[tuple[int, int]]:
		return self.id_ranges
	

	def merge_ranges(self, id_ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
		sorted_ranges = sorted(id_ranges, key=lambda x: x[0])
		merged = []
		
		for current in sorted_ranges:
			if not merged or merged[-1][1] < current[0] - 1:
				merged.append(current)
			else:
				merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))
		
		return merged
	

	def get_ranges_count(self) -> list[int]:
		return [end-start+1 for start, end in self.id_ranges]