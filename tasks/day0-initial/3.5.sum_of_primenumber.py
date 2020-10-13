r_number = 47

print ('Prime number Series -> ', end='')
sum = 0
for numb  in range(2,r_number+1):
	for num in range(2,numb):
		if(numb % num) == 0:
			break
	else:
		print(numb,' ',end='')
		sum += numb
print("")
print("The sum of the above prime number is ->", sum)