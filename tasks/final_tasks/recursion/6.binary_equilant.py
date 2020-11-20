#Python Program to Find the Binary Equivalent of a Number Recursively
binary_list = []
def binary_convert(num):
	if num == 0:
		# print(binary_list)
		return binary_list
	else:
		res = num % 2
		binary_list.append(res)
		# print(num, res, binary_list)
		binary_convert(num//2)

def main():
	num = 7
	binary_convert(num)
	binary_list.reverse()
	print(' '.join(list(map(str, binary_list))))

if __name__ == '__main__':
	main()