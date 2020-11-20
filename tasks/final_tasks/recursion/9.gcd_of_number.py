# Python Program to Find the GCD of Two Numbers Using Recursion

def gcd(a, b):
	if(b==0):
		return a
	else:
		return gcd(b, a%b)

def main():
	in_1 = 12
	in_2 = 8

	res = gcd(in_1,in_2)
	print('GCD', res)

if __name__ == '__main__':
	main()