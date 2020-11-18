# Python Program to Form an Integer that has the Number of Digits at Ten's Place and the Least Significant Digit of the Entered Integer at One's Place

def main():
	number = 1234353

	num_string = str(number)
	print('New number : ', int(str(len(num_string)) + num_string[-1]))

if __name__ == '__main__':
	main()