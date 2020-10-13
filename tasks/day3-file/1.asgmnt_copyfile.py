import re

def file_read_write():
	r_fd = open('/home/siva/Sony-python/sony-presamplecode/tasks/day3/read_content.txt','rt')
	w_fd = open('/home/siva/Sony-python/sony-presamplecode/tasks/day3/samp_write.txt','w')
	while (True):
		line = r_fd.readline()
		print('Lines ->',line)
		w_fd.write(line)

		if(len(line) <= 0 ):
			break

	r_fd.close()
	w_fd.close()

def file_upper_case():
	r_fd = open('/home/siva/Sony-python/sony-presamplecode/tasks/day3/read_content.txt','rt')
	w_fd = open('/home/siva/Sony-python/sony-presamplecode/tasks/day3/samp_write.txt','w')
	while (True):
		line = r_fd.readline()
		line = line.upper()
		print('Lines ->',line)
		w_fd.write(line)
		if(len(line) <= 0 ):
			break
	r_fd.close()
	w_fd.close()

def file_togle_case():
	r_fd = open('/home/siva/Sony-python/sony-presamplecode/tasks/day3/read_content.txt','rt')
	w_fd = open('/home/siva/Sony-python/sony-presamplecode/tasks/day3/samp_write.txt','w')
	while (True):
		line = r_fd.readline()
		line = line.swapcase()
		print('Lines ->',line)
		w_fd.write(line)
		if(len(line) <= 0 ):
			break
	r_fd.close()
	w_fd.close()

def remove_hello_line():
	r_fd = open('/home/siva/Sony-python/sony-presamplecode/tasks/day3/read_content.txt','rt')
	w_fd = open('/home/siva/Sony-python/sony-presamplecode/tasks/day3/samp_write.txt','w')
	substr = 'Hello'
	while (True):
		line = r_fd.readline()
		# print('Pre Lines ->',line)
		if (line.count(substr) == 0):
			print('Lines ->',line)
			w_fd.write(line)
		if(len(line) <= 0 ):
			break
	r_fd.close()
	w_fd.close()

def remove_empty_line():
	r_fd = open('/home/siva/Sony-python/sony-presamplecode/tasks/day3/read_content.txt','rt')
	w_fd = open('/home/siva/Sony-python/sony-presamplecode/tasks/day3/samp_write.txt','w')
	substr = "\n"
	while (True):
		line = r_fd.readline()
		line_d = line.strip("\n")
		print('Pre Lines ->',line_d.find(substr))
		if (line_d.find(substr) != -1):
			print('Lines ->',line_d)
			w_fd.write(line)
		if(len(line) <= 0 ):
			break
	r_fd.close()
	w_fd.close()

def main():
	#file_read_write()
	# file_upper_case()
	# file_togle_case()
	# remove_hello_line()
	remove_empty_line()

if(__name__ == '__main__'):
	main()