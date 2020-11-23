# Python sample Fibinaci Series in generator

def myfibanacigen(no1, no2, terms):
	count = 0
	while count < terms:
		no1, no2 = no2, no1 + no2
		yield no1
		count += 1

def main():
	no1 = 0
	no2 = 1

	terms = 5

	mygen = myfibanacigen(no1, no2, terms)

	try:
		print(next(mygen), end= ', ')
		print(next(mygen), end= ', ')
		print(next(mygen), end= ', ')
		print(next(mygen), end= ', ')
		print(next(mygen), end= ', ')
		print(next(mygen), end= ', ')
		print(next(mygen), end= ', ')
		print(next(mygen), end= ', ')
		print(next(mygen), end= ', ')
		print(next(mygen), end= ', ')
	except:
		print('\n','StopIteration Reached')

if __name__ == '__main__':
	main()