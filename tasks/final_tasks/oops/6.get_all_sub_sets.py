# Python Program to Create a Class and Get All Possible Subsets from a Set of Distinct Integers
class Allsubsets():

	def subsets(lis):
		print(lis)
		

def main():
	list_ = []
	a = int(input('Enter no of elements : '))

	for _ in range(a):
		a = input('Enter the value : ')
		list_.append(a)
	# print(list_)

	obj = Allsubsets.subsets(list_)


if __name__ == '__main__':
	main()