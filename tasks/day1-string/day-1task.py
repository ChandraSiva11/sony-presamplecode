import sys
import re

f1 = sys.argv[1]
f2 = sys.argv[2]

print("input 1 and 2",f1, f2)

f1 = open('/home/siva/Sony-python/sony-presamplecode/tasks/day1/'+f1,'r')
f1_lines = f1.readlines()
# print(f1_lines)
f1_matchcount = 0
for f1_line in range(0,len(f1_lines)-1):
	match1 = re.search('warning',f1_lines[f1_line])
	if match1 :
		# print('file1_lines -> ',f1_lines[f1_line])
		f1_matchcount += 1
	# input()
print('File1 warnings count ->', f1_matchcount)

f2 = open('/home/siva/Sony-python/sony-presamplecode/tasks/day1/'+f2,'r')
f2_lines = f2.readlines()
# print(f2_lines)

f2_matchcount = 0
for f2_line in range(0,len(f2_lines)-1):
	match2 = re.search('warning',f2_lines[f2_line])
	if match2:
		# print('File2 lines -> ',f2_lines[f2_line])
		f2_matchcount += 1
	# input()
print('File2 warnings count ->', f2_matchcount)

if (f1_matchcount <= f2_matchcount):
	print('Build not prompted because warnings count got increased')
else:
	print('Build prompted')