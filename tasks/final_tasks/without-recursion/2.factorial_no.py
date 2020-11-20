# Python Program to find the factorial of a number without recursion

def main():
	num = 6
	fact = 1
	for i in range(num,0,-1):
		fact *= i
	print('Result : ', fact)

if __name__ == '__main__':
	main()