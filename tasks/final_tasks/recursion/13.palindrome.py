# Python Program to Check Whether a String is a Palindrome or not Using Recursion

def reverse(str_no):
	if len(str_no) < 1:
		return True
	else:
		if str_no[0] == str_no[-1]:
			return reverse(str_no[1:-1])
		else:
			return False


def main():
	no = 123321
	str_no = str(no)
	res = reverse(str_no)

	if res:
		print(no, ' : is palindorme')
	else:
		print(no, ' : is not palindrome')

if __name__ == '__main__':
	main()