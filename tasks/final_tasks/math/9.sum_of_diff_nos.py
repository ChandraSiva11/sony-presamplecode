# Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List

def main():
	in_list = [1, 3, 8, 9, -2, -3, 12]
	neg_list = []
	even_list = []
	odd_list = []
	for i in in_list:
		if i < 0:
			neg_list.append(i)
		else:
			if i % 2 == 0:
				even_list.append(i)
			else:
				odd_list.append(i)
	print('Sum of Negative number', sum(neg_list))
	print('Sum of Even numbers', sum(even_list))
	print('Sum of Odd number', sum(odd_list))


if __name__ == '__main__':
	main()