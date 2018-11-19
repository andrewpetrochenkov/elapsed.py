#!/usr/bin/env python
import datetime
import time
import elapsed

dt = datetime.datetime.now()
time.sleep(2)
print("elapsed.get(datetime): %s" % elapsed.get(dt))
print("")
print("elapsed.seconds(datetime): %s" % elapsed.seconds(dt))
print("elapsed.minutes(datetime): %s" % elapsed.minutes(dt))
print("elapsed.hours(datetime): %s" % elapsed.hours(dt))
print("elapsed.days(datetime): %s" % elapsed.days(dt))
