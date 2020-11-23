# Prime Series program between 1 to 100

def main():
	for i in range (1,100):
		flag = 0
		# print(i)
		for j in range(2, i):

			if i % j == 0:
				flag = 1
				break
		if flag == 0:
			print(i, end = ', ')

if __name__ == '__main__':
	main()