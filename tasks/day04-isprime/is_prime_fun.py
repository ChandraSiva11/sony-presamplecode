
def is_prime(num):
	# print('Type ->',type(num))
	if isinstance(num,int):
		if (num >= 100):
			print('Input value is more than 100')
			return False
		elif(num < 100 and num > 0):
			print('Input value is in between 0 and 100')
			return True
		else:
			return False
	else:
		print('Its not integer')
		return False


def main():
	inputs = [1,2,3,4,5,6,1000,1.0,-20,137,59,'siva']
	for ele in inputs:
		ret_val = is_prime(ele)
		if(ret_val == True):
			print(ele, 'Input is validated and it is with in range ->', ret_val)
		else:
			print(ele, 'Input is validated and its not not in range ->', ret_val)
	

if ( __name__ == '__main__'):
	main()