#Removing duplicates while maintaining the original ordering of elements

def dedupe(items):
  seen = set()
  for item in items:
    if item not in seen:
      yield item
      seen.add(item)

row = [1,2,5,6,7,7,3,4,1,2,4,2,4,8,5,7]
unique_items = dedupe(row)

for unique_item in unique_items:
  print unique_item
  
'''
Output:
1
2
5
6
7
3
4
8
'''
