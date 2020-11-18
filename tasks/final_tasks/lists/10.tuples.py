# Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number

def main():
	list_a = [1,3,5,8]


	square = [(a,a**2) for a in list_a]
	print(square)

if __name__ == '__main__':
	main()