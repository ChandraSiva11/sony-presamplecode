#Python Program to Remove the nth Index Character from a Non-Empty String

def main():
	string = 'Hellow Siva! welcome to advanced python'
	rem = 2

	print(string[0:rem] + string[rem+1:])


if __name__ == '__main__':
	main()