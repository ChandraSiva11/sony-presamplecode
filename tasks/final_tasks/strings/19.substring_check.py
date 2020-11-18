# Python Program to Check if a Substring is Present in a Given String

def main():
	string = 'String for substring checking'
	sub_str = 'for'

	res = string.find(sub_str)
	if res != -1:
		print(res, 'Substring found on the string :')
	else:
		print('Substring not found')

if __name__ == '__main__':
	main()