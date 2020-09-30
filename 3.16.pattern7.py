# ord -> gives the unicode of character
# chr -> gives the character value
# print(ord('D'))
# print(chr(68))

max_num = 5
asci = 65

k = max_num + 1
for i in range(0, max_num):
	for j in range(0 , k):
		print(end="  ")
	k = k - 1
	for j in range(0 , i*2 + 1 ):
		print(chr(asci+j), end=" ")
	print("")
#---------------------------------------------------------
k = max_num//2 -1
for i in range(max_num , -1, -1):
	for j in range(k , 0 , -1): 
		print(end="  ")
	k = k + 1
	for j in range(0 , i*2 + 1):
		print(chr(asci+j), end=" ")
	print("")
