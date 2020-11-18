# Python Program to Print Numbers in a Range (1,upper) Without Using any Loops

def printfr(upper):
	if (upper > 0):
		print(upper)
		printfr(upper - 1)
		print(upper)

def main():
	upper_limit = 5
	printfr(upper_limit)


if __name__ == '__main__':
	main()