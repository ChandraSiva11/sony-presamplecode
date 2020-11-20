# Python Program to Find the Factorial of a Number Using Recursion
def fact(number):
	if number == 1:
		return 1
	else:
		return (number * fact(number-1))


def main():
	number = 5
	res = fact(number)
	print("Res", res)

if __name__ == '__main__':
	main()