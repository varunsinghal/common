#Priority queue developed with heapq module

import heapq

class PriorityQueue:
  def __init__(self):
    self.queue = []
    self._index = 0
    
  def push(self, item, priority):
    heapq.heappush(self.queue, (-priority, self._index, item))
    self._index += 1
  
  def pop(self):
    return heapq.heappop(self._queue)[-1]
    
q = PriorityQueue()
q.push('a', 1)
q.push('b', 4)
q.push('c', 5)
q.push('d', 1)

q.pop()
#Output: 'c'
q.pop()
#Output: 'b'
q.pop()
#Output: 'a'

  
