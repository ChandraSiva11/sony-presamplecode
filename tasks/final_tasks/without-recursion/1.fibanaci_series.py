# Python Program to Find the Fibonacci Series without Using Recursion

def main():
	first  = 1
	second = 1
	terms = 10
	# for ()
	print(first, second, end=' ')

	for i in range(0, terms):
		first, second = second, first + second
		print(second, end=' ')

if __name__ == '__main__':
	main()