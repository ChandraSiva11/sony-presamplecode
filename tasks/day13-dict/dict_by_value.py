"""Module strint"""


def main(dictionary):
	print('Input Dictionary ->', dictionary)
	new_dict = dict((v.lower(), k) for k, v in dictionary.items())
	print('\tNew swap dictionary', new_dict)

	print("key for the value one 		: %d" % new_dict['One'.lower()])
	print("key for the value two 		: %d" % new_dict['Two'.lower()])
	print("key for the value three		: %d" % new_dict['thREE'.lower()])
	print("key for the value four 		: %d" % new_dict['four'.lower()])
	print("key for the value five 		: %d" % new_dict['fiVe'.lower()])
	print("key for the value six 		: %d" % new_dict['Six'.lower()])
	print("key for the value sevan		: %d" % new_dict['seven'.lower()])
	print("key for the value eight		: %d" % new_dict['eight'.lower()])
	print("key for the value nine		: %d" % new_dict['nine'.lower()])


if __name__ == '__main__':
	dict_ = {1 : 'one', 2: 'two', 3: 'three', 4 : 'Four', 5 : 'fiVe', 6 : 'six', 7 : 'Seven', 8 : 'eight', 9 : 'nine'}
	main(dict_)