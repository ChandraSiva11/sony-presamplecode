max_val = 9
space = max_val
for j in range(1,max_val+1):
	print(' '*space,end='')
	for i in range(1,j+1):
		print(i,end='')
	max_val -= 1
	space -= 1
	print('')