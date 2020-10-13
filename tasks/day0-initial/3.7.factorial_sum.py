num = 5

fact = 1
summ = 0
for i in range(1,num+1):
	fact *= i
	summ += fact
	print (fact," ",end='')
print("")
print("Factorial Sum of all numbers of above seriese --> ", summ)