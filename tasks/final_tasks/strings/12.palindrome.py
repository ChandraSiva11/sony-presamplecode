# Python Program to Check if a String is a Palindrome or Not

def main():
	string = 'aabbaa'

	str_rev = string[::-1]

	if string == str_rev:
		print("The given string is Palindrome")
	else:
		print("String is not palindrome")

if __name__ == '__main__':
	main()