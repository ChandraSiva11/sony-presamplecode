# Python Program that Reads a Text File and Counts the Number of Times a Certain Letter Appears in the Text File

def main():
	word = 'is'
	fd = open('text_doc.txt', 'r')
	word_count = 0
	for line in fd.readlines():
		words = line.split()
		for wd in words:
			if word == wd:
				word_count +=1
	fd.close()
	print(word,' Match wrord Count', word_count)

if __name__ == '__main__':
	main()