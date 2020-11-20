# Python Program to Find the Power of a Number Using Recursion

def power(base, expo):
	if expo == 0:
		return 1
	else:
		return base * power(base, expo - 1)

def main():
	base_no = 5
	exp_no = 2
	res = power(base_no, exp_no)
	print("Result", res)

if __name__ == '__main__':
	main()