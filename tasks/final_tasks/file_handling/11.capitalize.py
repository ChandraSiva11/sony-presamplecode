# Python Program to Read a File and Capitalize the First Letter of Every Word in the File

def main():
	with open('text_doc.txt', 'r') as fread:
		for line in fread:
			print(line.title())

if __name__ == '__main__':
	main()