# Python Program to Accept a Hyphen Separated Sequence of Words as Input and Print the Words in a Hyphen-Separated Sequence after Sorting them Alphabetically

def main():
	string = 'This-is-the-sample-input'
	str_li = string.split('-')
	res = sorted(str_li)

	print('-'.join(res))

if __name__ == '__main__':
	main()