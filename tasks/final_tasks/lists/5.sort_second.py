
# sorting based on second element in sub list

def main():
	list_a = [[4,2],[1,3],[2,1],[11,21],[6,4]]

	for i in range(0,len(list_a)):
		print(i)
		for j in range(i+1, len(list_a)):
			if list_a[i][1] > list_a[j][1]:
				list_a[i], list_a[j] = list_a[j], list_a[i]

	print(list_a)



if __name__ == '__main__':
	main()