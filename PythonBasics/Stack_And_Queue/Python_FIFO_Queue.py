
# Python FIFO Queue (called queue))
"""
The python Queue model also provides the LifoQueue class, which implements a basic LIFO collection.
Items can be added to the head of the container using put(), and removed from the head using get().

FIFO Queue constructor:
class queue.LifoQueue(maxsize=0)
where-
The queue size is infinite if the maxsize is negative or zero.
"""

import queue

q = queue.Queue()

#put items at the end of the queue
for x in range(4):
    q.put("item-" + str(x))

#remove items from the head of the queue
while not q.empty():
    print(q.get())

"""
  output:
item-0
item-1
item-2
item-3
"""