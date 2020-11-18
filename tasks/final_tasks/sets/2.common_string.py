# Python Program to Check Common Letters in Two Input Strings

def main():
	str1 = 'This is the first text'
	str2 = 'This is the second text'

	a = set(str1)
	b = set(str2)
	c = a.intersection(b)
	print('Common Letters ', c)

if __name__ == '__main__':
	main()