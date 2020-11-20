# Python Program to Find the Total Sum of a Nested List Using Recursion
def summariation(list_):
	# def sum1(lst):
    total = 0
    for element in list_:
        if (type(element) == type([])):
            total = total + summariation(element)
        else:
            total = total + element
    return total

def main():
	nes_list = [[1,2],[3,4],[5,6]]
	res = summariation(nes_list)
	print('Result : ', res)

if __name__ == '__main__':
	main()