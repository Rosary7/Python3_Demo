# Threads using 'threading' module
# Syntax: _thread.start_new_thread ( function, args[, kwargs] )
"""
Note:
    Use 'threading' module instead of '_thread' module.
"""
import threading
import time

exitFlag = 0

class ThreadDemo (threading.Thread):
   def __init__(self, threadID, name, delay, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.delay = delay
      self.counter = counter

   def run(self):
      print ("Starting child thread " + self.name)
      show_data(self.name, self.delay, self.counter)
      print ("Exiting child thread " + self.name)

def show_data(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = ThreadDemo(1, "Thread-1", 2, 6)
thread2 = ThreadDemo(2, "Thread-2", 5, 6)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")