# Python Program to Find the Cumulative Sum of a List where the ith Element is the Sum of the First i+1 Elements From The Original List


def main():
	list_in = [1, 4, 7, 9, 8]
	new_list = []

	count = 0
	for li in list_in:
		new_list.append(count+li)
		count = li + count

	print("",list_in,"\n",new_list)

if __name__ == '__main__':
	main()