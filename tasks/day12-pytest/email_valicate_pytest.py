import pytest
import re


email_data = [
	{'email_d' : 'chad@abc.com', 'exp_re' : False},
	{'email_d' : 'chad@abc.com', 'exp_re' : True},
	{'email_d' : 'chan@qwe', 'exp_re' : False},
	{'email_d' : 'chand.com', 'exp_re' : False},
	{'email_d' : 'chand.123@com', 'exp_re' : False},
	{'email_d' : 'chand@siv.com', 'exp_re' : True},
	{'email_d' : 'chand@siv.com', 'exp_re' : False}
]


def regex_email_validation(email):
    regex = '^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$'
    # assert re.search(regex, email['email_d']) == email['exp_re'] , print(f"Test Failed Expected result is {email['exp_re']}")
    if(re.search(regex, email)):
    	return True
    #     print("Valid Email")
    else:
    	return False
    #     print("Invalid Email")


@pytest.mark.parametrize('email',email_data)
def test_email(email):
    rt_val = regex_email_validation(email['email_d'])
    print('Return Value', rt_val)
    assert rt_val == email['exp_re'], print(f"Test failed Expected result is {email['exp_re']}")
# test_email('chand.com')