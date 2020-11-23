# program for iterator domonstration, print number 10 to 15 using iterator
class Myiterator:

	def __init__(self, no_1, no_2):
		self.no_1 = no_1
		self.no_2 = no_2

	def __iter__(self):
		return self

	def __next__(self):
		no_1 = self.no_1
		if no_1 >= self.no_2:
			raise StopIteration
		self.no_1 = no_1 + 1
		return no_1


def main():
	no_1, no_2 = 10, 20
	obj = Myiterator(no_1, no_2)

	print(next(obj))
	print(next(obj))
	print(obj.__next__())
	# print(obj.__next__())
	# print(obj.__next__())
	# print(obj.__next__())
	# print(obj.__next__())
	# print(obj.__next__())
	# print(obj.__next__())

if __name__ == '__main__':
	main()