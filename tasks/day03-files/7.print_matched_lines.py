def main():
	string = """The file test.txt is opened using the open() function using the f stream. Each
Another file out.txt is opened using the open() function in the write mode using the f1 stream.
Each line in the file is iterated over using a for loop (in the input stream).
Each of the iterated lines is written into the output file. """

	substr = 'Each'
	for line in string.split('\n'):
		# print("Lines ->",line)
		if (line.startswith(substr)):
			# print('Match found on the line',line.startswith(substr))
			print('Lines with Each at start ->',line)


if(__name__ == '__main__'):
	main()