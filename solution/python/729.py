"""
https://leetcode.com/problems/my-calendar-i/solution/
"""
class MyCalendar(object):

    def __init__(self):
        self.schedules = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for s, e in self.schedules:
            if s < end and start < e:
                return False
        self.schedules.append([start, end])
        return True
