# Python Program to Concatenate Two Dictionaries Into One

def main():
	dict_1 = {"a" : 'siva'}
	dict_2 = {'b' : 'gokul'}

	dict_1.update(dict_2)

	print(dict_1)


if __name__ == '__main__':
	main()