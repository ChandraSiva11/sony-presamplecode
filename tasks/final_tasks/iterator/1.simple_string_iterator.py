# First Simple iterator progrma in python

def main():
	string = "Hi Hellow world"
	itr_obj = iter(string)

	# For loop will automatically handle the stop iteration
	# for i in itr_obj:
	# 	print(i)

	# With out for loop
	try :
		print(next(itr_obj))
		print(next(itr_obj))
		print(next(itr_obj))
		print(next(itr_obj))
		print(next(itr_obj))
		print(next(itr_obj))
		print(next(itr_obj))
		print(next(itr_obj))
		print(next(itr_obj))
		print(next(itr_obj))
		print(next(itr_obj))
		print(next(itr_obj))
		print(next(itr_obj))
		print(next(itr_obj))
		print(next(itr_obj))
		# print(next(itr_obj))


	except Exception as error:
		print('next iteration Error : ', error)



	# print(itr_obj)


if __name__ == '__main__':
	main()