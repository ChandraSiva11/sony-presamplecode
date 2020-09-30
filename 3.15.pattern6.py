max_val = 8
a = 0

for j in range (0,max_val+1):
	for i in range(0,2*max_val-1):
		if (i >= max_val):
			a -= 1
		else:
			a += 1
		if (a>j):
			print(' ',end='')
		else:
			print(a, end='')
	a = 0
	print("")