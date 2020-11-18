#Python Program to Form a New String where the First Character and the Last Character have been Exchanged

def main():
	string = 'This is the sample string'

	str_li = list(string)
	str_li[0], str_li[-1] = str_li[-1], str_li[0]
	print(''.join(str_li))


if __name__ == '__main__':
	main()