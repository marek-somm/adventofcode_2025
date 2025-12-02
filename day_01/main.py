from dial import Dial
from input import Input

dial = Dial(50)
input = Input('input.txt')

zero_counter = 0

while input.has_more():
	value = input.get_next()
	zero_counter += dial.turn_and_count_zeros(value)

print(f"Number of times dial reached zero: {zero_counter}")