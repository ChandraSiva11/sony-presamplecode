# Sample list iteration

def main():
	lst = ['siv', 'gokul', 'kannan']
	it_lst = iter(lst)

	# print(dir(lst),'\n\n','-'*185,'\n')
	# print(dir(it_lst))

	print(next(it_lst))
	print(next(it_lst))
	print(next(it_lst))
	print(next(it_lst))

if __name__ == '__main__':
	main()