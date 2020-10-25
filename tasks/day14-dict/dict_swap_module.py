class dict_swap(dict):


	def __init__(self,dict_):
		# print('Test -------->', type(dict_))
		for key, value in dict_.items():
			print (key, value)

	def __setitem__(self, key, value):
		print('Set Item called')
		if isinstance(value, str):
			value = value.lower()
		super().__setitem__(value, key)

	def __getitem__(self, key):
		print('-----------> Getitem called')
		if isinstance(key, str):
			key = key.lower()
		# if key in __setitem__:
		return super().__getitem__(dict_)
		# elif value in __setitem__:
		# 	return super().__getitem__(value)
