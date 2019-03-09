"""
[6, 28, 496, 8128, 33550336]
https://en.wikipedia.org/wiki/List_of_perfect_numbers
"""
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in [6, 28, 496, 8128, 33550336]