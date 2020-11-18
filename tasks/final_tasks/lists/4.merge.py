
#Python Program to Merge Two Lists and Sort it

def main():
	list_1 = [1,4,2,9,10,11]
	list_2 = [2,8,21,22,33,14]

	list_3 = list_1 + list_2
	list_3.sort()
	print(list_3)

	# Manual sorting
	# for i in range(0, len(list_3)):
	# 	for j in range (i+1, len(list_3)):
	# 		if list_3[i] > list_3[j]:
	# 			list_3[i],list_3[j] = list_3[j], list_3[i]
	# print(list_3)


if __name__ == '__main__':
	main()