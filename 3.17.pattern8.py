max_val = 5
asci = 65

sec_chr = 0
for i in range(max_val,0,-1):
	char_val = 0
	for j in range(i,0,-1):
		print(chr(asci+char_val),end='')
		char_val += 1
	for j in range(2*(max_val-i)):
		print(' ',end='')
	for j in range(i,0,-1):
		print(chr(asci+j-1),end='')
	print("")
for i in range(max_val):
	for j in range(i+1):
		print(chr(asci+j),end='')
		char_val = asci+j
	for j in range(2*(max_val-i-1)):
		print(' ',end='')
	for j in range(i+1):
		print(chr(char_val),end='')
		char_val -= 1
	print('')
