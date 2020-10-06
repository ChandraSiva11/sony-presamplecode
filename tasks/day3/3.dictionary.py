
def main():
	op_dict = {}
	string = """EDFFX2AD \dat_out_sig_reg[0]  ( .D(N69), .E(N96), .CK(clk), .Q(dat_out[0])
         );"""
	lists = string.split(' ',1)
	op_dict[lists[0]] = lists[1]
	print('Output Dictionary ->', op_dict)


if(__name__ == '__main__'):
	main()