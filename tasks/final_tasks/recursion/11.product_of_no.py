# Python Program to Find the Product of two Numbers Using Recursion
def product(a, b):
	if b == 0:
		return 0
	else:
		return a + product(a, b - 1)

def main():
	num1 = 7
	num2 = 10

	res = product(num1, num2)
	print('Result', res)

if __name__ == '__main__':
	main()