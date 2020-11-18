# Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

def main():
	n = 5

	dict_ = {i:i**2 for i in range(1, n+1)}

	print(dict_)


if __name__ == '__main__':
	main()