"""Module doc string"""


def clear_function(dictionary):
	print(f"Before clear Dictionary : {dictionary}")
	dictionary.clear()
	print(f"After clear Dictionary : {dictionary}")


def copy_function(dictionary):
	print("Copy a dictionary to another variable")
	dict_cpy = dictionary.copy()
	# dict_cpy = dictionary
	print(f"Copied dictionary : {dict_cpy}")


def fromkeys_function():
	tple = ['a', "b", "c"]
	m = 10
	dict_ = dictionary.fromkeys(tple, m)
	print("Created dictionary from iterable object : ", dict_)

def get_fuction(dictionary):
	# print(help(dictionary.get))
	name = dictionary.get('name')
	print('Get value of the dictionary ->', name)

def items_function(dictionary):
	# print(help(dictionary.items))
	print('Dictionary items print in list of tuples :', dictionary.items())


def keys_function(dictionary):
	print(f'Dictionary keys list print : {dictionary.keys()}')


def values_function(dictionary):
	print(f'Dictionary values list print : {dictionary.values()}')


def pop_function(dictionary):
	print(f"Dictionary Before pop : {dictionary}")
	ele = dictionary.pop('subject')
	print(f"Dictionary After pop subject : {dictionary} {ele}")


def pop_item(dictionary):
	# print(help(dictionary.popitem))
	print(f"Dictionary Before popitem : {dictionary}")
	ele = dictionary.popitem()
	print(f"Dictionary After popitem subject : {dictionary} {ele}")


def setdefault_function(dictionary):
	# print(help(dictionary.setdefault))
	print('Print Default keyvalue if key is not present in the dictionary for key name:',dictionary.setdefault('name', 'gokul'))


def update_function(dictionary):
	# print(help(dictionary.update))
	print('Dictionary Before update ->', dictionary)
	dictionary.update({'name' : 'gokul'})
	print('Dictionary After update ->', dictionary)
	# pass


if __name__ == '__main__':
	dictionary = {'name': 'siva', 'subject':'maths', 'marks':90}
	# clear_function(dictionary)
	# copy_function(dictionary)
	# fromkeys_function()
	# get_fuction(dictionary)
	# items_function(dictionary)
	# keys_function(dictionary)
	# values_function(dictionary)
	# pop_function(dictionary)
	# pop_item(dictionary)
	# setdefault_function(dictionary)
	update_function(dictionary)
