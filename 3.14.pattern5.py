max_val = 8

a = 0
space = 0
dup_max = max_val
while (max_val>0):
	for i in range(0,2*dup_max-1):
		if( i >= dup_max):
			a -= 1
		else:
			a += 1
		if(a<=max_val):
			print(a,end=' ')
		else:
			print(' '*2,end='')
	a = 0
	max_val -=1
	print('')
	# input()