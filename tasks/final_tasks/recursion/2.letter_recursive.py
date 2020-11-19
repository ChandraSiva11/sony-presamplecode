# Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively

def check_string(string, char):
	print('Length of string ', len(string))
	if len(string) == 1:
		return 0
	elif(string[0] == char):
		print('Match Test')
		return 1+ check_string(string[1:],char)
	else:
		print('Unmatch Test')
		return check_string(string[1:],char)

def main():
	string = 'This is the sample text'
	char = 'i'
	count = check_string(string, char)

	print(char, 'char Count in the string', count)

if __name__ == '__main__':
	main()