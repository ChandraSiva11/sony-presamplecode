#Python Program to Print Table of a Given Number

def main():
	num = 9

	for i in range(1,11):
		print(str(num) + ' * ' + str(i) + ' = ' + str(num*i))

if __name__ == '__main__':
	main()