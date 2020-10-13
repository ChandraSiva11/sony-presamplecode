
def main():
	string = """EDFFX2AD \dat_out_sig_reg[0]  ( .D(N69), .E(N96), .CK(clk), .Q(dat_out[0])
         );
  EDFFX2AD \dat_out_sig_reg[1]  ( .D(N70), .E(N94), .CK(clk), .Q(dat_out[1])
         );
  EDFFX2AD \dat_out_sig_reg[2]  ( .D(N71), .E(N92), .CK(clk), .Q(dat_out[2])
         );
  DFFQXLAD \dat_out_sig_reg[8]  ( .D(N77), .CK(clk), .Q(dat_out[8]) );DFFQXLAD
  DFFQXLAD \dat_out_sig_reg[15]  ( .D(N84), .CK(clk), .Q(dat_out[15]) );
  DFFQXLAD \dat_out_sig_reg[6]  ( .D(N75), .CK(clk), .Q(dat_out[6]) );
  DFFQXLAD \dat_out_sig_reg[11]  ( .D(N80), .CK(clk), .Q(dat_out[11]) );"""

	substr1 = "EDFFX2AD"
	substr2 = "DFFQXLAD"

	count1 = string.count(substr1)
	count2 = string.count(substr2)

	print('String Match count ->', count1 + count2)


if(__name__ == '__main__'):
	main()