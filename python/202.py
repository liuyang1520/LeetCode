# Use a set to record all numbers, if there is a repetition, return false.
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        trace = set()
        while n != 1:
            trace.add(n)
            temp = str(n)
            total = 0
            for i in temp:
                total += int(i) ** 2
            if total == 1:
                return True
            if total in trace:
                return False
            n = total