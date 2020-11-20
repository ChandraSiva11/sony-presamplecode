#Python Program to Find if a Number is Prime or Not Prime Using Recursion
def is_prime(a, b):
	if b == 1:
		return True
	if a % b == 0:
		return False
	else:
		# print(a, b)
		return is_prime(a, b-1)


def main():
	no = 12

	value = is_prime(no, no//2+1)
	if value:
		print(no, ' is a prime number')
	else:
		print(no, 'is not a prime number')

if __name__ == '__main__':
	main()