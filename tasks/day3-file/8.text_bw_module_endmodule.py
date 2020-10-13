def main():
	fd = open('read_content.txt','rt')
	count = 0
	start_str = 'module'
	end_str = 'endmodule'
	flag = 0
	for line in fd:
		# print ('Lines ->',line)
		if(flag == 0):
			if( line.find(start_str) != -1):
				# print('Test1',line.find(start_str))
				flag = 1
				count += 1
		else:
			if(line.find(end_str) == -1):
				# print('Test2',line.find(end_str))
				count += 1
			else:
				count -= 1
				# print('Test3',line.find(end_str))
				break
	fd.close()
	print('Number of lines between module and endmodule ->',count)


if (__name__ == '__main__'):
	main()