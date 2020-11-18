#Python Program to Find Those Numbers which are Divisible by 7 and Multiple of 5 in a Given Range of Numbers

def main():
	start = 10
	end =500

	for i in range(start, end):
		if i % 7 == 0 and i % 5 == 0 :
			print(i)

if __name__ == '__main__':
	main()