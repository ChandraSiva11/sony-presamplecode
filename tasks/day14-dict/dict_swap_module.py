class dict_swap(dict):

	def __setitem__(self, key, value):
		if isinstance(value, str):
			value = value.lower()
		super().__setitem__(value, key)

	def __getitem__(self, key):
		if isinstance(key, str):
			key = key.lower()
		return super().__getitem__(key)
