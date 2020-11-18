# Python Program to Compute the Value of Euler's Number e. Use the Formula: e = 1 + 1/1! + 1/2! + …… 1/n!
import math

def main():
	terms = 10
	sum = 0

	for i in range(1, terms+1):
		sum += 1/math.factorial(i)

	print('Sum of the series : ', round(sum,2))


if __name__ == '__main__':
	main()