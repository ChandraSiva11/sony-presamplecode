# Python Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 10

def main():
	u_limit = 10
	list_out = []
	for i in range(1, u_limit):
		square = i**2
		string = str(square)
		# print(list(string))
		res = list(string)
		squr = map(int, res) 
		if sum(squr) <10:
			list_out.append(square)
	print(list_out)

if __name__ == '__main__':
	main()