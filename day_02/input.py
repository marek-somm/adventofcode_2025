
class Input:
	
	def __init__(self, filepath: str):
		self.id_ranges = self.read_id_ranges(filepath)
		self.ids = [id for r in self.id_ranges for id in self.convert_ranges_to_list(r)]
	

	def read_id_ranges(self, filepath: str) -> list:
		with open(filepath, 'r') as file:
			line = file.readline().strip()
			return [item.strip() for item in line.split(',')]
		
	
	def convert_ranges_to_list(self, range_str: str) -> list:
		start_str, end_str = range_str.split('-')
		start, end = int(start_str), int(end_str)
		return list(range(start, end + 1))
	

	def is_valid_id(self, id: int) -> bool:
		id_string = str(id)
		
		for divisor in self.get_divisors(id):
			parts = self.split_id_into_parts(id, divisor)
			if all(part == parts[0] for part in parts):
				return False
		

		half_index = len(id_string) // 2
		return id_string[:half_index] != id_string[half_index:]
	

	def get_divisors(self, id: int) -> list:
		n = len(str(id))

		return [k for k in range(2, n + 1) if n % k == 0]
	

	def split_id_into_parts(self, id: int, group_count: int) -> list:
		n = len(str(id))
		group_size = n // group_count
		return [str(id)[i:i + group_size] for i in range(0, n, group_size)
    ]
	

	def get_ids(self) -> list:
		return self.ids