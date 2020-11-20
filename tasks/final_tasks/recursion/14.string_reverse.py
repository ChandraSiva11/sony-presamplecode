# Python Program to Reverse a String Using Recursion

def revstring(string):
	if (len(string) == 0):
		return string
	else:
		# print(string)
		return revstring(string[1:]) + string[0]

def main():
	string = 'Sample test string'

	res = revstring(string)
	print(res)

if __name__ == '__main__':
	main()