# Python Program to Read Height in Centimeters and then Convert the Height to Feet and Inches

def main():
	in_cms =  45
	inches=0.394*in_cms
	feet=0.0328*in_cms
	print('Length in inches', round(inches))
	print('Length in feet', round(feet))


if __name__ == '__main__':
	main()