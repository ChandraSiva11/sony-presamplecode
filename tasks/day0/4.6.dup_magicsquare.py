
# result (25*26/2)/5

squair_size = 5

if(squair_size % 2 !=0 ):
	# print('Entered number is the odd number')

	magicsqr=[]
	for j in range(0,squair_size):
		row_array = []
		for i in range(0,squair_size):
			row_array.append(0)
		magicsqr.append(row_array)
	i = 0
	j = squair_size//2
	value = 1

	magicsqr[i][j] = 1
	while(True):
		value += 1	
		if( i == 0  and j != squair_size-1):
			i = squair_size-1
			j += 1
			print('-----------test 1--', i, j)
			if(i == squair_size and j == squair_size//2):
				break
		elif (j == squair_size-1 and i !=0):
			i -=1
			j =0
			print('-----------test 2--', i, j)
		elif(j > squair_size-1):
			j = 0
			# i -= 1
			print('-----------test 3--', i, j)
		elif(i == 0 and j == squair_size-1):
			i += 1
			# j -= 1
			print('-----------test 4--', i, j)
		elif (magicsqr[i-1][j+1] != 0 ):
			i += 1
			j += 1
			print('-----------test 5--', i, j)
		else:
			print('-----------test 6--', i, j)
			
			if (i == j):
				j += 1
			i -= 1
			# break
		if(i < squair_size and j < squair_size):
			magicsqr[i][j]=value
		
		if(i == squair_size and j == squair_size//2):
			break
		print('i and j values ->',i,j)
		input()
	for i in range (squair_size):
		for j in range(squair_size):
			print(format(magicsqr[i][j],'<4'),end= ' ')
		print('')
# print(magicsqr)

else:
	print('This technique will work only for the odd numbers')