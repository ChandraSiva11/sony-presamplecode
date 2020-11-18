#Python Program to Generate all the Divisors of an Integer

def main():
	num = 122

	for i in range(1, num//2 +1):
		if num % i == 0:
			print(i)


if __name__ == '__main__':
	main()