"""Test module doc string"""
import pytest

def is_valid_email(email):
	list1 = email[0].split('@')
	if len(list1) == 2:
		return True
	else:
		return False

emails = [{"data" : 'chandra@123@12', "exp_result" : True}, {"data" : 'chan@ka.n.com', "exp_result" : True}, {"data" :'chan@kan', "exp_result" : False}, {"data" :'chandru', "exp_result" : False}, {"data" :'chan.com', "exp_result" : False}]
# emails = ['chandra@123', 'chan@kan.com', 'chan@kan', 'chandru', 'chan.com']
@pytest.mark.parametrize("email", emails)
def test_is_valid_email(email):
	print('List Email', email["data"], end=' ')
	rt_val = is_valid_email(email["data"])
	try:
		assert email['exp_result'] == rt_val, 'Assertion failed'
	except AssertionError as error:
		print(error)

# test_is_valid_email('chandra@123@12')