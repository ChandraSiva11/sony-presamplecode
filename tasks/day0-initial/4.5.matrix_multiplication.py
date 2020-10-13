row = int(input('Enter the number of rows in matrix1 : '))
row_clmn = int(input('Enter the number of rows in matrix1 or no of columns in matrix2: '))
colmn = int(input('Enter the number of columns in matrix2 : '))

print('\n\nReading the matrix1 from user input')
matrix1=[]
for j in range(0,row):
	row_array = []
	for i in range(0,row_clmn):
		row_array.append(int(input('Please enter the array1 row elemets :')))
	matrix1.append(row_array)

print('\n\nReading the matrix2 from user input')
matrix2=[]
for j in range(0,row_clmn):
	row_array = []
	for i in range(0,colmn):
		row_array.append(int(input('Please enter the array1 row elemets :')))
	matrix2.append(row_array)


print('\n\nPrinting the matrix1 value in matrix format')

for i in range (row):
	for j in range(row_clmn):
		print(format(matrix1[i][j],'<3'),end= ' ')
	print('')

print('\n\nPrinting the matrix1 value in matrix format')

for i in range (row_clmn):
	for j in range(colmn):
		print(format(matrix2[i][j],'<3'),end= ' ')
	print('')

print('\n\n Multiplication of two matrixes')

result=[]
for j in range(0,row):
	row_array = []
	for i in range(0,colmn):
		row_array.append(0)
	result.append(row_array)
print(result)

for i in range(0,row):
	for j in range (0,colmn):
		for k in range(0,row_clmn):
			result[i][j] = result[i][j] + (matrix1[i][k] * matrix2[k][j])

print('Result of Multiplication of two matrices')
for i in range (row):
	for j in range(colmn):
		print(format(result[i][j],'<3'),end= ' ')
	print('')

print('result array1 ->', result)