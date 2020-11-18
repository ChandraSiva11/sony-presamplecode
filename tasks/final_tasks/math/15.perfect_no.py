# Python Program to Check if a Number is a Perfect Number

def main():
	num = 7
	sum_ = 0
	for i in range(1, num):
		if num % i == 0:
			sum_ += i
	if sum_ == num :
		print('Given number is ths perfect number', num)
	else:
		print('Given number is not a perfect number', num)

if __name__ == '__main__':
	main()