# Python Program to Print all the Prime Numbers within a Given Range

def main():
	num = 50
	prime = []
	for i in range(2, num+1):
		flag = 0
		for j in range(2, i//2 +1):
			if i % j == 0:
				flag = 1
		if flag == 0:
			prime.append(i)
	print('Prime list', prime)

if __name__ == '__main__':
	main()