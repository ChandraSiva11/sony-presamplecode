r_number = 47

print ('Prime number Series -> ', end='')

for numb  in range(2,r_number+1):
	for num in range(2,numb):
		if(numb % num) == 0:
			break
	else:
		print(numb,' ',end='')
print("")

