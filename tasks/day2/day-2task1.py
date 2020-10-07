import sys

f0 = sys.argv[0]
f1 = sys.argv[1]
f2 = sys.argv[2]

path = '/'.join(f0.split('/')[:-1])
substr = 'warning'

def main():
	f1_content = open(path+'/'+f1,'r')
	content1 = f1_content.read()
	war1_count = content1.count(substr)
	print('Number of warnigs file1 ->',war1_count)

	f2_content = open(path+'/'+f2,'r')
	content2 = f2_content.read()
	war2_count = content2.count(substr)
	print('Number of warnigs file2 ->',war2_count)

	if(war1_count >= war2_count):
		print('Build prompted')
	else:
		print('Build not prompted, because warnings count increased')

if __name__ == '__main__':
	main()