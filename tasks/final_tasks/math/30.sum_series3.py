# Python Program to Find the Sum of the Series: 1 + x^2/2 + x^3/3 + … x^n/n

def main():
	x = 7
	t = 10
	sum = 0
	for i in range(1, t+1):
		sum += x**i / i
	print('Sum of the series : ', round(sum, 2))

if __name__ == '__main__':
	main()