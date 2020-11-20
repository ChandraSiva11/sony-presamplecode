# Python Program to Read the Contents of a File in Reverse Order
def main():
	fdr = open('text_doc.txt', 'r')
	for line in reversed(list(fdr)):
		print(line.rstrip())

if __name__ == '__main__':
	main()