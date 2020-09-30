max_val = 7
a = 0

for i in range(0,2*max_val-1):
	
	if (i >= max_val):
		a -= 1
	else:
		a += 1

	print(a," ", end='')
print("")