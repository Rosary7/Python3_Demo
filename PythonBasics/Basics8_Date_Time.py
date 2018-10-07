# Date and Time

import time
import calendar

x = time.time()
# Clearly, this isn’t very human-readable. :)
print(x)
print()

print (time.localtime())
print()

# Getting the Formatted Time
print (time.asctime())
print()

# gmtime() converts the current time into UTC (GMT)
print (time.gmtime())
print()

# sleep() holds the execution for a given amount of seconds.
print (time.asctime())
time.sleep(2)
print (time.asctime())
print()

# get the calendar for - Oct 2018
print (calendar.month(2018,10))
print()


