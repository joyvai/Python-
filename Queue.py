
#queue means first-in and first-out

from collections import deque

queue = deque (["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
print queue.popleft() # it pops the first index value
print deque
print queue

