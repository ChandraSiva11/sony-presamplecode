arr = [1,2,3,3,5,6,1,9]

size = len(arr)

for i in range(0,size):
	for j in range(i+1,size):
		if(arr[i] == arr[j]):
			print('Duplicate -> ', arr[j])
			arr[j] = 0
print('Result array -> ',arr)