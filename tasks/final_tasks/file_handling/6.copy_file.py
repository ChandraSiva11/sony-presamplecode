# Python Program to Copy the Contents of One File into Another

def main():
	with open('text_doc.txt', 'r') as fr:
		# print(help(open))
		with open('text_doc2.txt', 'w') as fw:
			for line in fr:
				fw.write(line)

if __name__ == '__main__':
	main()