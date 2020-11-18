# Python Program to Find the Area of a Triangle Given All Three Sides
import math

def main():
	a = 10
	b = 13
	c = 15

	s = (a + b + c)/2

	area = math.sqrt(s * (s - a) * (s - b) * (s - c))
	print('Area of the Triangle', round(area, 2))

if __name__ == '__main__':
	main()