# Python Program to Check if a Number is a Prime Number

def main():
	num = 13
	flag = 0
	for i in range(2, num):
		if num % i == 0 :
			flag += 1
	if flag == 0:
		print(num, "Number is a prime number")
	else:
		print(num, "Number is not a prime number")

if __name__ == '__main__':
	main()