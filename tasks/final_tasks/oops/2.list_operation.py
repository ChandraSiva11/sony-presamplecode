# Python Program to Append, Delete and Display Elements of a List Using Classes
class Listoperation():

	def __init__(self, ):
		self.name = [1, 4, 5]

	def add(self, ele):
		return self.name.append(ele)
		# pass

	def remove(self, ele):
		return self.name.remove(ele)
		# pass

	def display(self):
		return self.name
		# pass


def main():
	class_object = Listoperation()
	print('Initial value ',class_object.name)

	# ADD through object
	class_object.name.append(2)
	print('After adding one element',class_object.name)

	# Remove through object
	class_object.name.remove(2)
	print('After removing one element',class_object.name)

	#Add through class function add
	class_object.add(7)
	print('Add Element by class fun',class_object.name)

	#Remove through class function remove
	class_object.remove(7)
	print('Remove Element by class fun',class_object.name)

	res = class_object.display()
	print('Display vlaue print', res)

if __name__ == '__main__':
	main()