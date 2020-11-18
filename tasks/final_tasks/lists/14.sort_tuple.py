#Python program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple

def main():
	li_tpl = [(2,1,4),(4,1,6),(3,9,1),(1,4,2),(6,4,8),(17,5,21)]

	for i in range(0,len(li_tpl)):

		for j in range(i, len(li_tpl)):

			if li_tpl[i][-1] > li_tpl[j][-1] :
				li_tpl[i], li_tpl[j] = li_tpl[j], li_tpl[i]

	print(li_tpl)



if __name__ == '__main__':
	main()