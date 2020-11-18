# Python Program to Count the Occurrences of Each Word in a Given String Sentence

def main():
	string = 'This is the the the sample input sentence'
	word_input = 'the'

	words = string.split()
	cnt = 0
	for word in words:
		if word_input == word:
			cnt += 1

	print(word_input, 'Repeated times', cnt)


if __name__ == '__main__':
	main()