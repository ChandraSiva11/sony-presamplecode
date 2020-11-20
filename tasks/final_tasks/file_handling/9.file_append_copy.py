# Python Program to Append the Contents of One File to Another File

def main():
	with open('text_doc.txt', 'r') as fr:
		# print(help(open))
		with open('text_doc2.txt', 'a') as fw:
			for line in fr:
				fw.write(line)

if __name__ == '__main__':
	main()