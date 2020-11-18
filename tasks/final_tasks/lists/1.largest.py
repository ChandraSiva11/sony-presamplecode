
#Python Program to Find the Largest Number in a List
from functools import reduce

def main():
	in_list = [1,2,3,4,5,32, 7,9,8]
	res = reduce(lambda x,y : x if x>y else y, in_list)
	print(res)


if __name__ == '__main__':
	main()