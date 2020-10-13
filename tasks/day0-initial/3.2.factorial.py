num = 15

fact = 1
for i in range(1,num+1):
	fact *= i
	print (fact," ",end='')

print("")
print('Factorial Value of ',num,' is ->', fact)