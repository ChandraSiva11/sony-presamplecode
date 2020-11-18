#Python Program to Take the Temperature in Celcius and Covert it to Farenheit

def main():
	cel_input = 12
	faran_heat = (cel_input * 1.8 ) + 32

	print('Farenheit output', round(faran_heat))

if __name__ == '__main__':
	main()