# Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

def main():
	string_1 = 'This is the first string with highest length'
	string_2 = 'smaller length string'

	count1 = 0
	count2 = 0

	for char in string_1:
		count1 += 1
	for char in string_2:
		count2 += 1

	if (count1 > count2):
		print('First string in grater length :', count1)
	elif (count1 < count2):
		print('Second string is grater length :', count2)
	else:
		print('Both the strings are equal')

if __name__ == '__main__':
	main()