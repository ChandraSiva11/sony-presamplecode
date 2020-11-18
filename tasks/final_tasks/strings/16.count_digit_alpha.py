# Python Program to Calculate the Number of Digits and Letters in a String

def main():
	string = "This is the 1 sample 4 input for 3 digit2 and letters count55"
	char_count = 0
	num_count = 0
	for char in string:
		if char.isalpha():
			char_count += 1
		elif char.isdigit():
			num_count += 1
	print(char_count, num_count)

if __name__ == '__main__':
	main()