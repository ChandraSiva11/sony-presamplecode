# Python Program to Check if a Date is Valid and Print the Incremented Date if it is


def main():
	date_input = '31/9/2020'

	dd, mm, yy = date_input.split('/')
	dd = int(dd)
	mm = int(mm)
	yy = int(yy)

	if (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
		mml = 31
	elif(mm == 4 or mm == 6 or mm == 9 or mm == 11):
		mml = 30
	elif (mm == 2):
		if (yy %4 == 0 and yy%100 != 0 or yy%400 == 0):
			mml = 29
		else:
			mml = 28
	# print(type(dd))
	if (dd < 1 or dd > mml):
		print ('1Invalid date given')
	elif (dd >1 and dd != mml):
		dd += 1
		print('2Valid date, Next day :', str(dd)+'/'+str(mm)+'/'+str(yy))
	elif (dd == mml and mm == 12):
		mm = 1
		dd = 1
		yy += 1
		print('3Valid date, Next day :', str(dd)+'/'+str(mm)+'/'+str(yy))
	elif (dd == mml and mm !=12):
		dd = 1
		mm += 1
		print ('4Valid date, Next day :', str(dd)+'/'+str(mm)+'/'+str(yy))
	elif (mm <1 or mm > 12):
		print('5Invalid month of date given')
	else:
		dd +=1
		print ('7Valid date, Next day :', str(dd)+'/'+str(mm)+'/'+str(yy))

if __name__ == '__main__':
	main()