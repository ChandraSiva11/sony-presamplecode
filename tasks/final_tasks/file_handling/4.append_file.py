# Python Program to Read a String from the User and Append it into a File

def main():
	fd = open('text_doc_write.txt', 'a')
	fd.write('write line on the file\n')
	fd.close()

if __name__ == '__main__':
	main()