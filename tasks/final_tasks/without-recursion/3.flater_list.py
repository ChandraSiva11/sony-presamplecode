# Python Program to Flatten a List without using Recursion
def main():
	lis = [[1,2],[3,4],[5,6,7,8]]
	fat = []
	for li_ele in lis :
		if isinstance(li_ele, list):
			for ele in li_ele:
				fat.append(ele)
		else:
			fat.append(li_ele)
	print(fat) 


if __name__ == '__main__':
	main()