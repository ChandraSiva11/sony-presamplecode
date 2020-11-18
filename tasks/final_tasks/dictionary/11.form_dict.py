# Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character

def main():
	string = 'This is the string for testing'
	li_str = string.split()
	dict_ = {}

	for word in li_str:
		dict_[word[0]] = word
	print(dict_)

if __name__ == '__main__':
	main()