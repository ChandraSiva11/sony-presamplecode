# Python Program that Displays which Letters are Present in Both the Strings

def main():
	str1 = 'This was the string1'
	str2 = 'This is the string2'

	a = set(str1)
	b = set(str2)
	c = a.union(b)
	print('Elements common for both the sets ',c)

if __name__ == '__main__':
	main()