# Python Program that Displays which Letters are in the Two Strings but not in Both

def main():
	str1 = 'first string for testing'
	str2 = 'second string for test'

	print(set(str1)^set(str2))

if __name__ == '__main__':
	main()