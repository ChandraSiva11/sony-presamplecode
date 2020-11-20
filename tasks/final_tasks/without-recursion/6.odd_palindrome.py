#Python Program to Find All Numbers which are Odd and Palindromes Between a Range of Numbers without using Recursion

def main():
	f_no =100
	l_no =150

	res = [x for x in range(f_no, l_no +1) if x%2 != 0 and str(x) == str(x)[::-1]]
	print(res)

if __name__ == '__main__':
	main()