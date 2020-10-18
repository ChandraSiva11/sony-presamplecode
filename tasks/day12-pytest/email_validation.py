"""Test module doc string"""
import pytest

def is_valid_email(email):
	list1 = email[0].split('@')
	if len(list1) == 2:
		return True
	else:
		return False


# emails = ['chandra@123', 'chan@kan.com', 'chan@kan', 'chandru', 'chan.com']
@pytest.mark.parametrize(email, [['chandra@123@12', True], ['chan@ka.n.com', True], ['chan@kan', False], ['chandru', False], ['chan.com', False]])
def test_is_valid_email(email):
	print('List Email', email)
	ret_val = is_valid_email(email[0])
	try:
		assert email[1] == ret_val, 'Assertion failed'
	except AssertionError as error:
		print(error)


# test_is_valid_email('chandra@123@12')