#Python Program to Multiply All the Items in a Dictionary

def main():
	dict_ = {"a" : 19, 'b' :21, 'm' : 11}

	res = 1
	for i in dict_.values():
		res = i * res
	print('Result : ', res)

if __name__ == '__main__':
	main()