# Custom Fibnaci Seriese
class Fibnaci():

	def __init__(self, no1, no2):
		self.no1 = no1
		self.no2 = no2
		self.count= 0

	def __iter__(self):
		return self

	def __next__(self):
		no2 = self.no2
		# self.no1 = self.no2
		# self.no2 = self.no1 + self.no2
		self.no1, self.no2 = self.no2, self.no1 + self.no2
		self.count += 1
		if self.count > 10:
			raise StopIteration
		else:
			return no2


def main():
	# 1, 1, 2, 3, 5, 8, 13, 21.....
	no1 = 1
	no2 = 1

	obj = Fibnaci(no1, no2)
	# print(dir(obj))
	print(no1, end= ', ')
	print(next(obj), end= ', ')
	print(next(obj), end= ', ')
	print(next(obj), end= ', ')
	print(next(obj), end= ', ')
	print(next(obj), end= ', ')
	print(next(obj), end= ', ')
	print(next(obj), end= ', ')
	print(next(obj), end= ', ')
	print(next(obj), end= ', ')
	print(next(obj), end= ', ')
	# print(next(obj), end= ', ')



if __name__ == '__main__':
	main()