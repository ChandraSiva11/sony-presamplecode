# Python Program to Check if a Given Key Exists in a Dictionary or Not

def main():
	dict_ = {'a' : 'aaa', 'b' : 'bbb', 'c' : 'ccc'}

	ele = 'd'

	if ele in dict_ :
		print('Element is in the dictionary : ', ele)
	else:
		print('Element is not in the dictionary : ', ele)

if __name__ == '__main__':
	main()