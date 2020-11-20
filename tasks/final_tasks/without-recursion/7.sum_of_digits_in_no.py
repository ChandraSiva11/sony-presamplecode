#Python Program to Find the Sum of Digits in a Number without Recursion

def main():
	number = 12345
	str_no = str(number)
	res = list(map(int,str_no))
	print('Result :',sum(res))

if __name__ == '__main__':
	main()