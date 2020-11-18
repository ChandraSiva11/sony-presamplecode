# Python Program that Displays which Letters are in the First String but not in the Second

def main():
	str1 = 'This is string156'
	str2 = 'This is string2'

	a = set(str1)
	b = set(str2)

	c = a.difference(b)

	print(dir(a))
	print(c)

if __name__ == '__main__':
	main()