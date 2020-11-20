# Python Program to Find the Binary Equivalent of a Number without Using Recursion
def main():
	num = 43

	lis = []
	while True:
		lis.append(num % 2 )
		num = num//2
		if num == 0:
			break
	lis.reverse()
	res = list(map(str, lis))
	print(' '.join(res))

if __name__ == '__main__':
	main()