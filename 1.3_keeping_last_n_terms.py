#Keeping only last N terms in memory

from collections import deque
d = deque(maxlen=3)
d.append(1)
d.append(2)
d.append(3)
print d
d.append(4)
print d

'''
The complexity of inserting or removing an element from the list data type is O(N). 
But in the case of deque the complexity reduces to O(1).
'''
