# Python Program to Find the Sum of First N Natural Numbers

def main():
	number = 10
	sum = 0
	for i in range(1, number +1):
		sum += i
	print('Sum of Natural numbers = ', sum)

if __name__ == '__main__':
	main()