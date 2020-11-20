# Python Program to Find the Sum of Elements in a List Recursively
def sum_array(list_, size):
	if size == 0:
		return 0
	else:
		return list_[size - 1] + sum_array(list_, size -1 )

def main():
	list_ = [1, 3, 5, 2, 7, 9]
	size = len(list_)

	result = sum_array(list_,size)
	print('Sum of list is ', result)


if __name__ == '__main__':
	main()