"""
Math problem
https://discuss.leetcode.com/topic/18054/4-lines-o-log-n-c-java-python/2
"""
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        div, digit = 1, 0
        while n >= div:
            quo, digit, rem = n / (div*10), n / div % 10, n % div
            if digit > 1:
                res += (quo + 1) * div
            elif digit == 1:
                res += quo * div + rem + 1
            else:
                res += quo * div
            div = div * 10
        return res