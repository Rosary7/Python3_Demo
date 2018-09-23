# Threads using '_thread' module
# Syntax: _thread.start_new_thread ( function, args[, kwargs] )
"""
Note:
    Use 'threading' module instead of '_thread' module.
"""
import _thread
import time

def show_data(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))

# Create threads
try:
    _thread.start_new_thread(show_data, ('Thread1', 2))
    _thread.start_new_thread(show_data, ('Thread2', 5))
except:
    print('Unable to start thread-error')

while 1:
   pass