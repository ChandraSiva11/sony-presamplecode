#Python Program to Detect if Two Strings are Anagrams

def main():
	str_1 = [1, 2, 6, 4]
	str_2 = [1, 4, 2, 6]
	if sorted(str_1) == sorted(str_2):
		print('Yes, Two lists are Anagrams')
	else:
		print('Now, Two lists are not Anagrams')


if __name__ == '__main__':
	main()