#Python Program to Calculate the Length of a String Without Using a Library Function

def main():
	string = 'This is the sample text'
	# print(string.index(string[-1]))
	count = 0
	for char in string:
		count += 1
	print('Length', count)

if __name__ == '__main__':
	main()