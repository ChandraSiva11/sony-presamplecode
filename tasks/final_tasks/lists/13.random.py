#Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List
import random

def main():
	list_a = []

	for a in range(1,10):
		list_a.append(random.randint(1,20))

	print(list_a)

if __name__ == '__main__':
	main()