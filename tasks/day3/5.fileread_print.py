
def main():
	fd = open('/home/siva/Sony-python/sony-presamplecode/tasks/day3/read_content.txt','rt')
	while (True):
		line = fd.readline()
		print(line)
		if(len(line) <= 0 ):
			break

if(__name__ == '__main__'):
	main()