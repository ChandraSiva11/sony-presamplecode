def main():
	string = """w	wire   N69, N70, N71, N72, N73, N74, N75, N76, N77, N78, N79, N80, N81, N82,
         N83, N84, N86, N88, N90, N92, N94, N96, n42, n43, n44, n45, n46, n47;"""
	
	lists = string.split()
	print("Number of words ->", len(lists))

if(__name__ == '__main__'):
	main()