
class Grid:

	def __init__(self, lines: list[str]) -> None:
		self.grid = self.convert_lines_to_grid(lines)

	
	def convert_lines_to_grid(self, lines: list[str]) -> list[list[int]]:
		return [[int(char.replace("@","1").replace(".","0")) for char in line] for line in lines]
	

	def count_surrounding(self, x: int, y: int) -> int:
		count = 0
		for dy in [-1, 0, 1]:
			for dx in [-1, 0, 1]:
				nx, ny = x + dx, y + dy
				if (dx != 0 or dy != 0) and 0 <= ny < len(self.grid) and 0 <= nx < len(self.grid[0]):
					count += self.grid[ny][nx]
		return count
	

	def get_grid(self) -> list[list[int]]:
		return self.grid
	

	def get_value_at(self, x: int, y: int) -> int:
		return self.grid[y][x]
	

	def get_width(self) -> int:
		return len(self.grid[0]) if self.grid else 0
	

	def get_height(self) -> int:
		return len(self.grid)