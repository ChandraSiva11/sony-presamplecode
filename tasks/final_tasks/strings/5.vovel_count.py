# Python Program to Count the Number of Vowels in a String

def main():
	vov = ['a','e','i','o','u']

	string = 'The Python programming examples also contains programs on Strings.'
	count = 0
	for char in string:
		if char in vov:
			count += 1
	print('Number of Vovel count', count)

if __name__ == '__main__':
	main()