# Python Program to Count the Number of Words in a Text File
def main():
	num_words = 0
	with open('text_doc.txt', 'r') as f:
		for line in f:
			words = line.split()
			num_words += len(words)
	print('Number of words', num_words)



if __name__ == '__main__':
	main()