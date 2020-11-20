# Python Program to Read the Contents of a File

def main():
	fdr = open('text_doc.txt', 'r')
	content = fdr.read()
	print(content)
	fdr.close()

if __name__ == '__main__':
	main()