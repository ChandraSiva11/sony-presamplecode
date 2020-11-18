# Python Program to Check if a Number is an Armstrong Number

def main():
	a = 371
	b = list(map(int, str(a)))
	res = list(map(lambda x: x**3, b))

	if sum(res) == a :
		print('Given nmber is Amstrong number : ', a)
	else:
		print('Given number is not Amstrong number : ', a)


if __name__ == '__main__':
	main()