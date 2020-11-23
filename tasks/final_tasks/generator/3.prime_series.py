# prime series using generator

def mygeneratorfun():

	for i in range(1, 20):
		flag = 0
		for j in range(2,i):
			if i %j == 0:
				flag = 1
				break
		if flag == 0:
			yield i

def main():
	# mygeneratorfun(term)
	mygen = mygeneratorfun()
	try:
		print(next(mygen))
		print(next(mygen))
		print(next(mygen))
		print(next(mygen))
		print(next(mygen))
		print(next(mygen))
		print(next(mygen))
		print(next(mygen))
		print(next(mygen))
		print(next(mygen))
	except:
		print('StopIteration')

if __name__ == '__main__':
	main()