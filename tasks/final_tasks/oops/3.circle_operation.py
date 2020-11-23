# Python Program to Create a Class and Compute the Area and the Perimeter of the Circle
class Circle():

	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return 22*self.radius**2/7

	def perimeter(self):
		return 2*22*self.radius/7


def main():
	obj = Circle(44)
	print('Area', round(obj.area(),2))
	print('Perimeter', round(obj.perimeter(),2))


if __name__ == '__main__':
	main()