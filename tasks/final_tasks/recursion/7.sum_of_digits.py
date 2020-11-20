# Python Program to Find the Sum of the Digits of the Number Recursively

def summation(digits, length):
	if length < 0:
		return 0
	else :
		# print(length, digits[length])
		return int (digits[length]) + summation(digits, length-1)

def main():
	num = 8391

	digits = str(num)
	length = len(digits)
	res = summation(digits, length -1 )
	print('Result -> ', res)


if __name__ == '__main__':
	main()