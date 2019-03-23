#!/usr/bin/env python
import datetime
import os
import public

"""
ps -p %s -o etime
http://pubs.opengroup.org/onlinepubs/9699919799/utilities/ps.html
[[dd-]hh:]mm:ss
"""


@public.add
class Elapsed(int):
    __readme__ = ["seconds", "minutes", "hours", "days", "__init__", "__str__"]

    def __new__(cls, seconds):
        """init from total seconds count"""
        return super(Elapsed, cls).__new__(cls, seconds)

    @property
    def seconds(self):
        """return elapsed time in seconds"""
        return int(self)

    @property
    def minutes(self):
        """return elapsed time in minutes"""
        return int(int(self) / 60)

    @property
    def hours(self):
        """return elapsed time in hours"""
        return int(self.minutes / 60)

    @property
    def days(self):
        """return elapsed time in days"""
        return int(self.hours / 24)

    def __str__(self):
        """format elapsed time in the form `[[dd-]hh:]mm:ss`"""
        string = "%02d:%02d" % (self.minutes % 60, int(self) % 60)
        if self.hours:
            string = "%02d:%s" % (self.hours % 24, string)
        if self.days:
            string = "%s-%s" % (self.days, string)
        return string

    def __repr__(self):
        return self.__str__()


def _parse_ps_output(string):
    """parse `ps -p <pid> -o etime` output and return total seconds count"""
    t = string.replace('-', ':').split(':')
    t = [0] * (4 - len(t)) + [int(i) for i in t]
    seconds = t[0] * 86400 + t[1] * 3600 + t[2] * 60 + t[3]
    return seconds


@public.add
def get(input=None):
    """return elapsed.Elapsed instance. accepts pid or datetime"""
    if isinstance(input, datetime.datetime):
        return Elapsed((datetime.datetime.now() - input).total_seconds())
    if not input or isinstance(input, int):
        pid = input if input else os.getpid()
        output = os.popen("ps -p %s -o etime | grep -v ELAPSED" % pid).read().strip()
        if output:
            return Elapsed(_parse_ps_output(output))


@public.add
def seconds(input=None):
    """return elapsed time in seconds. accepts pid or datetime"""
    return int(get(input))


@public.add
def minutes(input=None):
    """return elapsed time in minutes. accepts pid or datetime"""
    return get(input).minutes


@public.add
def hours(input=None):
    """return elapsed time in hours. accepts pid or datetime"""
    return get(input).hours


@public.add
def days(input=None):
    """return elapsed time in days. accepts pid or datetime"""
    return get(input).days
