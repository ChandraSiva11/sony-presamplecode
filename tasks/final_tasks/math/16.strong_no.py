# Python Program to Check if a Number is a Strong Number

def main():
	num = 146
	str_num = str(num)
	num_li = list(map(int, str_num))
	fact_li = []

	for i in num_li:
		fact = 1
		for j in range(i, 0, -1):
			fact = fact * j
		fact_li.append(fact)
	
	if sum(fact_li) == num:
		print('The Given number is the Strong number', num)
	else:
		print('The Given number is not a Strong number', num) 


if __name__ == '__main__':
	main()