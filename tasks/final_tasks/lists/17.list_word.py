#Python Program to Read a List of Words and Return the Length of the Longest One

def main():
	string = 'This is the test script for finding words with longest lenngth'

	str_list = string.split()
	max_length = 0
	long_word  = ''

	for word in str_list:
		if len(word) > max_length:
			max_length = len(word)
			long_word = word
		elif len(word) == max_length:
			long_word += ', '+ word
		else:
			pass

	print('Long words :', long_word, max_length)

if __name__ == '__main__':
	main()