# Python Program to Create a Class in which One Method Accepts a String from the User and Another Prints it
class Printclass():

	def __init__(self):
		self.string = ''

	def get(self):
		self.string = input("Enter the input String : ")

	def put(self):
		print('Printing value : ', self.string)

def main():
	obj = Printclass()
	obj.get()
	obj.put()

if __name__ == '__main__':
	main()