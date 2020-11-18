# Python Program to Find the LCM of Two Numbers

def main():
	first_num = 3
	sec_num = 6

	max1 = max(first_num, sec_num)

	while (True):
		if max1 % first_num == 0 and max1 % sec_num == 0:
			print('Lcm of the given number is ', max1)
			break
		max1 += 1


if __name__ == '__main__':
	main()