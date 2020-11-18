
#Python Program to Sort a List According to the Length of the Elements
def main():
	str_list = ['abc', 'lkddd', 'a', 'mm']

	for i in range(0, len(str_list)):
		for j in range(i, len(str_list)):
			if len(str_list[i]) > len(str_list[j]):
				str_list[i], str_list[j] = str_list[j], str_list[i] 
	print(str_list)

	# str_list.sort(key=len)
	# print(str_list)

if __name__ == '__main__':
	main()