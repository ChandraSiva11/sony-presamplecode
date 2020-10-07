arr = [2,1,5,40,8,9,5,20]

size = len(arr)
for i in range(0,size-1):
	for j in range(i+1,size):
		if arr[i] <= arr[j] :
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp

print('Sorted Array', arr)