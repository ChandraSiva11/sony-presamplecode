#Python Program to Find the Gravitational Force Acting Between Two Objects

def main():
	m1 = 1000000
	m2 = 500000
	r = 20
	G = 6.673 * (10**-11)

	f = G * m1* m2 / r**2

	print('Force Between 2 mass', round(f, 2), 'N')

if __name__ == '__main__':
	main()