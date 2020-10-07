import re
import functools

a='123'
b = re.split(r'',a)
b.pop(0)
b.pop(-1)
res = functools.reduce(lambda i, j: int(i) + int(j) , b)
res1 = ' + '.join(b)
print('sum ->', res1,' = ', res)
