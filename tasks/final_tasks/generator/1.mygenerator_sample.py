# Simple Generator Example
def mygeneratorfun():
	yield 1
	yield 2
	yield 3

def main():
	gen = mygeneratorfun()
	# print(next(gen))
	# print(next(gen))
	# print(next(gen))
	try:
		print(gen.__next__())
		print(gen.__next__())
		print(gen.__next__())
		print(gen.__next__())
		print(gen.__next__())
	except StopIteration:
		print('StopIteration reached')
	
if __name__ == '__main__':
	main()