import re

a='626'
b = re.split(r'',a)
b.pop(0)
b.pop(-1)
b.reverse()
c = ''.join(b)
if a == c:
    print('Yes, because the reverse of ',a, ' is also ', c)