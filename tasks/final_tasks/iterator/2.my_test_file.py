# sample script for checking iterator

class Myclass():

	def __siv__(self):
		print('Siva')

def main():
	obj = Myclass()
	# print(dir(Myclass))
	print(dir(obj.__ge__(1)))

if __name__ == '__main__':
	main()