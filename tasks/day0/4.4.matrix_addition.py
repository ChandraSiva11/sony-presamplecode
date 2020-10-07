
row = int(input('Enter the number of matrix row : '))
colmn = int(input('Enter the number of matrix column : '))

print('\n\nReading the matrix1 from user input')
matrix1=[]

for j in range(0,colmn):
	row_array = []
	for i in range(0,row):
		row_array.append(int(input('Please enter the array1 row elemets :')))
	matrix1.append(row_array)

print('\n\nReading the matrix2 from user input')
matrix2=[]
for j in range(0,colmn):
	row_array = []
	for i in range(0,row):
		row_array.append(int(input('Please enter the array1 row elemets :')))
	matrix2.append(row_array)


print('\n\nPrinting the matrix1 value in matrix format')

for i in range (row):
	for j in range(colmn):
		print(format(matrix1[i][j],'<3'),end= ' ')
	print('')

print('\n\nPrinting the matrix1 value in matrix format')

for i in range (row):
	for j in range(colmn):
		print(format(matrix2[i][j],'<3'),end= ' ')
	print('')

print('\n\nAddition of two Matrix ')

result = []
for j in range(0,colmn):
	row_array = []
	for i in range(0,row):
		row_array.append(0)
	result.append(row_array)

for i in range (0,row):
	for j in range(0,colmn):
		result[i][j] = matrix1[i][j] + matrix2[i][j]

print('Addition of the two matrix is')

for i in range (row):
	for j in range(colmn):
		print(format(result[i][j],'<3'),end= ' ')
	print('')

# print('Matrix1 ->',matrix1)
# print('Matrix2 ->',matrix2)
# print('Matrix2 ->',result)