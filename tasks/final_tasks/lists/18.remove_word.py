#Python Program to Remove the ith Occurrence of the Given Word in a List where Words can Repeat

def main():
	in_list = ['aaa','abc','aaa','cad','nmk','aaa','bca']
	rmv = 'aaa'
	ocr = 2

	cnt = 0
	out_list = []
	for name in in_list:
		if name == rmv:
			cnt += 1

			if cnt >= ocr:
				out_list.append(name)

	print('Repeated elements more than 2 occurances', out_list)
	print('Unique elements', set(in_list))
	print('Repeated Times', cnt)


if __name__ == '__main__':
	main()