# Python Program to Calculate the Number of Words and the Number of Characters Present in a String

def main():
	string = 'This the sample string'
	no_of_char = len(string)
	list_ = string.split()
	no_of_word = len(list_)
	print(no_of_char, no_of_word)
if __name__ == '__main__':
	main()