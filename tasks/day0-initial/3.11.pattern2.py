max_val = 9
space = 1
while (max_val >= 1):
	for i in range(1,max_val+1):
		print(i,end='')
	print('')
	print(' '*space,end='')
	max_val -=1
	space += 1
print('')