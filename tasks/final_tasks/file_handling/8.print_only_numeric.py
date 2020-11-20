# Python Program to Read a Text File and Print all the Numbers Present in the Text File

def main():
	with open('text_doc.txt', 'r') as fread:
		digit_count = 0
		for line in fread:
			for char in line:
				if char.isdigit():
					digit_count += 1
					print(char)

	print('Number of digits count : ', digit_count)

if __name__ == '__main__':
	main()