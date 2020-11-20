# Python Program to Count the Number of Lines in a Text File

def main():
	with open('text_doc.txt', 'r') as f:
		lines = f.readlines()
	print('Number of lines ',len(lines))

if __name__ == '__main__':
	main()