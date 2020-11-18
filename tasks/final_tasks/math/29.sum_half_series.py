# Python Program to Find the Sum of the Series: 1 + 1/2 + 1/3 + ….. + 1/N

def main():
	sum = 0
	num = 10
	for i in range(1,num):
		sum += 1/i
	print('Sum of the series :', round(sum, 2))

if __name__ == '__main__':
	main()