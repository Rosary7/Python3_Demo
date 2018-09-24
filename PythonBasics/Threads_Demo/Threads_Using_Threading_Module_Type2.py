# Threads using 'threading' module
"""
Note:
    Using 'threading' module and by passing a callable object to the constructors
"""
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def funA():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')

d = threading.Thread(name='Thread-1', target = funA)
d.setDaemon(True)

def funB():
    logging.debug('Starting')
    logging.debug('Exiting')

t = threading.Thread(name='Thread-2', target = funB)

d.start()
t.start()

d.join()
t.join()