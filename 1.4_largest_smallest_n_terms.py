#Finding the largest N or smallest N terms from a given sequence

import heapq

row = [2,3,4,5,2,3,4,1,765,23,434,2,1,21,13,2334,35,654,3,23,21,76,43]
print heapq.nsmallest(3, row)
#Output: [1, 1, 2]

record = [
  {'name': 'A', 'marks': 34},
  {'name': 'B', 'marks': 22},
  {'name': 'C', 'marks': 14},
  {'name': 'D', 'marks': 33},
  {'name': 'E', 'marks': 65},
  {'name': 'F', 'marks': 10}
  ]
print heapq.nlargest(2, record, key=lambda x: x['marks'])
#Output: [{'name': 'E', 'marks': 65}, {'name': 'A', 'marks': 34}]
