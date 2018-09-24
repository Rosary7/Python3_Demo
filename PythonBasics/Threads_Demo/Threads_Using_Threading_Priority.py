# Thread riority Queue
"""
This example has multiple threads consuming the jobs, which are processed based on the priority of items in the queue at the time get() was called.
The order of processing for items added to the queue while the consumer threads are running depends on thread context switching.

__cmp__ was removed in Python3, you should use the rich comparison dunder methods instead __lt__, __le__, __eq__, __ne__, __gt__, __ge__.

"""

import functools
import queue
import threading

@functools.total_ordering
class Job:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
        return

    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented


q = queue.PriorityQueue()

q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))


def process_job(q):
    while True:
        next_job = q.get()
        print('Processing job:', next_job.description)
        q.task_done()


workers = [
    threading.Thread(target=process_job, args=(q,)),
    threading.Thread(target=process_job, args=(q,)),
]
for w in workers:
    # A "daemon thread" flag signifies that the entire Python program exits when only daemon threads are left.
    w.setDaemon(True)
    w.start()

q.join()