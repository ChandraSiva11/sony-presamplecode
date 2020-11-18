# Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String

def main():
	string = "The sample TexT"

	up_count = 0
	lw_count = 0

	for char in string:
		if char.islower():
			lw_count += 1
		elif char.isupper():
			up_count += 1
	print(up_count, lw_count)

if __name__ == '__main__':
	main()