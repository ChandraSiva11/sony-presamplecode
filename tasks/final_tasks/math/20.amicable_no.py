# Python Program to Check If Two Numbers are Amicable Numbers

def main():
	no_1 = 220
	no_2 = 284
	
	sum_1 = 0
	sum_2 = 0
	
	for i in range(1, no_1):
		if no_1 % i :
			sum_1 += i
	
	for i in range(1, no_2):
		if no_1 % i :
			sum_2 += i

	if sum_1 == sum_2 :
		print("The given two numbers are amicable nos : ", no_1, no_2, sum_2, sum_1)
	else:
		print("The given two numbers are NOT amicable : ", no_1, no_2, sum_2, sum_1)


if __name__ == '__main__':
	main()