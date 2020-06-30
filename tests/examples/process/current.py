#!/usr/bin/env python
import time
import elapsed

time.sleep(2)
print("elapsed.get: %s" % elapsed.get())
print("elapsed.get.seconds: %s" % elapsed.get().seconds)
print("elapsed.get.minutes: %s" % elapsed.get().minutes)
print("elapsed.get.hours: %s" % elapsed.get().hours)
print("elapsed.get.days: %s" % elapsed.get().days)
print("")
print("elapsed.seconds(): %s" % elapsed.seconds())
print("elapsed.minutes: %s" % elapsed.minutes())
print("elapsed.hours: %s" % elapsed.hours())
print("elapsed.days: %s" % elapsed.days())
