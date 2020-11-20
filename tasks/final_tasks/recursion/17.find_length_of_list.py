# Python Program to Find the Length of a List Using Recursion
def length(list_):
	if not list_:
		return 0
	else:
		return 1 + length(list_[1:])

def main():
	list_ = [1,4,2,7,5,3,9,7,9]
	res = length(list_)
	print('Length of list : ', res)

if __name__ == '__main__':
	main()