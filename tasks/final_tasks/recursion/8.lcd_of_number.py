#Python Program to Find the LCM of Two Numbers Using Recursion
def lcm(num1,num2):
	lcm.multiple += num1
	if ((lcm.multiple % num1) == 0 and (lcm.multiple % num2 == 0)):
		return lcm.multiple
	else:
		lcm(num1,num2)
	return lcm.multiple


def main():
	num1 = 5
	num2 = 10
	lcm.multiple = 0

	if num2 > num1 :
		res = lcm(num1, num2) # small, big
	else:
		res = lcm(num2, num1) # small, big
	print('Result', res)


if __name__ == '__main__':
	main()