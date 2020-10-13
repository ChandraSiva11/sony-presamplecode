num = 20

n_fact = 1
np_fact = n_fact + 1
np_val = 2
summ = 0
for i in range(1,num+1):
	n_fact *= i
	np_fact = n_fact * np_val
	np_val += 1
	print (int(np_fact/n_fact)," ",end='')
print("")
