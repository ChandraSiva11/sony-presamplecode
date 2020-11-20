# Python Program to Count the Number of Blank Spaces in a Text File

def main():
	space_count = 0
	with open('text_doc.txt', 'r') as fread:
		for line in fread:
			for char in line:
				if char.isspace():
					space_count += 1
					# print(char)
	print('Space Count :', space_count)

if __name__ == '__main__':
	main()