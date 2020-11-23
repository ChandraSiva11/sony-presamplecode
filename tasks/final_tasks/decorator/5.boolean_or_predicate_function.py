# Program to understand the Boolean or Predicate function
def is_vowel(char):
	if char in 'aeiou':
		return True
	else:
		return False

def vowels(string):
	# print('Before convert to lower : ',id(string), string)
	string = string.lower()
	# print('After convert to lower : ',id(string), string)
	count = 0
	for i in string:
		if is_vowel(i):
			count += 1
	return count


def main():
	string = 'This is the input text for predicate function learning'
	print('There are ', vowels(string), 'Vowels found in the input string')




if __name__ == '__main__':
	main()