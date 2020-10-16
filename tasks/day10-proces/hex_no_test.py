li = []

for a in range (0, 5):
	# print(a)
	li.append(hex(a))
	print(a, '-->', hex(a))
print('Hex list ->', '[%s]' % ', '.join(map(str, li)))
