	
def main():
	tlist = [
			'Hello world',
			"Bye World",
			"I am in this world",
			"hi I am"
		]
	sub_str = 'world'
	count = 0

	for line in (tlist):
		if(line.lower().find(sub_str.lower()) == -1):
			# print('Match not found ->', line)
			pass
		else:
			# print('Match found ->', line)
			count += 1

	print('Case insensitive match foud ->',count)

if(__name__ == '__main__'):
	main()