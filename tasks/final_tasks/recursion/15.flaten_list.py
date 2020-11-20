#Python Program to Flatten a Nested List using Recursion

def flaten(nested_list):
	if nested_list == []:
		return nested_list
	if isinstance(nested_list[0], list):
		return flaten(nested_list[0]) + flaten(nested_list[1:])
	return nested_list[:1] + flaten(nested_list[1:])

def main():
	list_nested = [[1,2],[3,4]]
	result = flaten(list_nested)
	print(result)

if __name__ == '__main__':
	main()