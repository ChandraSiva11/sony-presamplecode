# Python Program to Find the Area of a Rectangle Using Classes

class Rectangle():
	def __init__(self, width, length) :
		self.width = width
		self.length = length

	def area(self):
		return self.width * self.length


def main():
	obj = Rectangle(20,4)
	obj2 = Rectangle(10,4)
	
	print(obj.area(), obj2.area())

if __name__ == '__main__':
	main()