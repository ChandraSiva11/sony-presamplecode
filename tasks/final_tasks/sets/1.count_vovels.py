# Python Program to Count the Number of Vowels Present in a String using Sets

def main():
	string = 'Python Program to Count the Number of Vowels Present in a String using Sets'
	vov = {'a','e','i','o','u'}
	count = 0
	for char in string:
		if char in vov:
			count += 1
	print('Vovel Count ', count)

if __name__ == '__main__':
	main()