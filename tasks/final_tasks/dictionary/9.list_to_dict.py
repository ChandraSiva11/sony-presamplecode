# Python Program to Map Two Lists into a Dictionary 

def main():
	list_1 = ['a', 'b', 'c', 'd']
	list_2 = [1, 2, 3, 4]

	print(dict(zip(list_1, list_2)))

if __name__ == '__main__':
	main()