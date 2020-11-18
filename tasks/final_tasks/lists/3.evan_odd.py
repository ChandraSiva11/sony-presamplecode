
#Python Program to Put Even and Odd elements in a List into Two Different Lists

def main():
	i_list = [1,3,2, 8, 9, 10,22,11,0]
	odd = []
	even = []
	for i  in i_list:
		if i%2 == 0:
			even.append(i)
		else:
			odd.append(i)
	print(odd, even)


if __name__ == '__main__':
	main()