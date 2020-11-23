# Python Program to Create a Class which Performs Basic Calculator Operations
class Calculator():

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def add(self):
		return self.a + self.b

	def sub(self):
		return self.a - self.b

	def mul(self):
		return self.a * self.b

	def div(self):
		return self.a / self.b


def main():
	num1 = 10
	num2 = 9
	obj = Calculator(num1, num2)

	print('Addition\t\t', obj.add())
	print('Substraction\t', obj.sub())
	print('Multiplication\t', obj.mul())
	print('Division\t\t', round(obj.div(),2))



if __name__ == '__main__':
	main()