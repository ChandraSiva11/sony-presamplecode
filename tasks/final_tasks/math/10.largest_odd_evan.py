#Python Program to Print Largest Even and Largest Odd Number in a List

def main():
	list_a = [1,4, 8,3,9,18,91,22,43,89,5,6]
	odd_li = []
	even_li = []
	for i in list_a:
		if i%2 == 0:
			even_li.append(i)
		else:
			odd_li.append(i)
	print('Largest odd No ', sorted(odd_li)[-1])
	print('Largest even No ', sorted(even_li)[-1])

if __name__ == '__main__':
	main()