def main():
	fd = open('/home/siva/Sony-python/sony-presamplecode/tasks/day3/read_content.txt','rt')
	lines = fd.readlines()
	print("list of lines ->",lines)

if(__name__ == '__main__'):
	main()