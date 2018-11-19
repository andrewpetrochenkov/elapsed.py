#!/usr/bin/env python
import os
import time
import elapsed

pid = os.getpid()
print("pid: %s" % pid)
time.sleep(2)
print("elapsed.get: %s" % elapsed.get(pid))
print("")
print("elapsed.seconds: %s" % elapsed.seconds(pid))
print("elapsed.minutes: %s" % elapsed.minutes(pid))
print("elapsed.hours: %s" % elapsed.hours(pid))
print("elapsed.days: %s" % elapsed.days(pid))
