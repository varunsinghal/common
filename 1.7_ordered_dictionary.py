#Creating an ordered dictionary

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 3
d['spam'] = 4
d['apple'] = 12

for key in d:
  print key
  
'''  
Output:
foo
bar
spam
apple

'''
