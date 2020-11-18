
#Python Program to Find the Second Largest Number in a List Using Bubble Sort

def main():
	list_a = [1,3,6,9,29,13,17,21,2]

	for i in range(0,len(list_a)):
		for j in range(i, len(list_a)):
			if list_a[i] > list_a[j]:
				list_a[i], list_a[j] = list_a[j], list_a[i]
	print('Second Largest', list_a[1])


if __name__ == '__main__':
	main()