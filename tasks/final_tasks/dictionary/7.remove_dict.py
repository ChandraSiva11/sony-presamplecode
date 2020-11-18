# Python Program to Remove the Given Key from a Dictionary

def main():
	dict_ = {'a' : 'aaaa', 'b' : 'bbbb', 'c' : 'cccc'}
	rm_key = 'a'
	del dict_[rm_key]

	print(dict_)

if __name__ == '__main__':
	main()