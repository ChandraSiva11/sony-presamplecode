# Python Program to Form a Dictionary from an Object of a Class
class Dict(object):
	def __init__(self):
		self.m = 1
		self.n = 2

def main():
	obj = Dict()
	print(obj.__dict__)

if __name__ == '__main__':
	main()