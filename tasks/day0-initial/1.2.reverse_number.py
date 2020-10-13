import re

a='12378'

b = re.split(r'',a)
b.pop(0)
b.pop(-1)
b.reverse()
rev = ''.join(b)
print(a,'-> Reverse value ->', rev)