
# Python Program to Determine Whether a Given Number is Even or Odd Recursively


def check(n):
    if (n < 2):
        return (n % 2 == 0)
    print('N', n)
    return (check(n - 2))


if __name__ == '__main__':
	n = 20
	if(check(n)==True):
		print("Number is even!")
	else:
		print("Number is odd!")