nthterm = 20
num1, num2 = 0 , 1

count = 0
sum = 0

while (count < nthterm ):
    num3 = num2 + num1
    num1 = num2
    num2 =num3
    print( num3, ' ',end='')
    sum += num3
    count += 1
print("")
print ('Sum of ', nthterm, ' numbers in the Fibnaci series --> ', sum)