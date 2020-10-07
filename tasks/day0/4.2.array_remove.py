arr = [1,2,3,3,5,6,1,9,7,12,1,333]

res_arr = []
size = len(arr)

for i in range(0,size):
	for j in range(i+1,size+1):
		if(arr[i] not in res_arr):
			res_arr.append(arr[i])
print('Result array -> ',res_arr)