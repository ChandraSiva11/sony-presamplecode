#Python Program to Find the Fibonacci Series Using Recursion


def fibnaci(no1, no2, term):
	if term == 0:
		return
	print(no2, end=', ')
	fibnaci(no2, no1 + no2, term -1)
	

def main():
	no1 = 1
	no2 = 1
	term = 20
	print(no1, end= ', ')
	fibnaci(no1,no2,term)

if __name__ == '__main__':
	main()