# Python Program to Swap the First and Last Value of a List

def main():
	list_b = [1,3,2,9,0,45,23]
	list_b[-1], list_b[0] = list_b[0], list_b[-1]
	print(list_b)

if __name__ == '__main__':
	main()