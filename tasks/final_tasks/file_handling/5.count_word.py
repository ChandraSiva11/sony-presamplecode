# Python Program to Count the Occurrences of a Word in a Text File
def main():
	word = 'is'
	fd = open('text_doc.txt', 'r')
	# print(dir(fd))
	word_count = 0
	for line in fd.readlines():
		# print(line)
		words = line.split()
		for wd in words:
			if word == wd:
				word_count +=1
	fd.close()
	print('Match wrord Count', word_count)


if __name__ == '__main__':
	main()