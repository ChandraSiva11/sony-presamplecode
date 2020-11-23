# Custom class list iteration
class Listiterator():

	def __init__(self, lis):
		self.lis = lis
		self.indx = 0
		# print(self.lis)

	def __iter__(self):
		return self

	def __next__(self):
		indx = self.indx
		self.indx += 1
		if self.indx > len(self.lis):
			raise StopIteration
		return self.lis[indx]

def main():
	lst = ['gokulan', 'chandrasiva', 'kannan', 'muthulakshmi', 'sripadmanaban']
	obj = Listiterator(lst)
	print(next(obj))
	print(next(obj))
	print(next(obj))
	print(next(obj))
	print(next(obj))
	print(next(obj))



if __name__ == '__main__':
	main()