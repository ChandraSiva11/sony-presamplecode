# Python Program to Count Number of Lowercase Characters in a String

def main():
	string = 'The Sample tEXt String'

	count = 0
	for char in string:
		if char.islower():
			count += 1
	print('No of lowercase letter', count)

if __name__ == '__main__':
	main()