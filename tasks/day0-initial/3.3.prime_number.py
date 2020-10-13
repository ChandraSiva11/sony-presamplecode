num = 11


for i in range(2,num):
	if (num % i) == 0:
		print('Given number is not a Prime number because it is divisible by ', i)
		break
else:
	print("Given number is a prime number -> ",num)
