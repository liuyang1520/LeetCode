"""
Use a dictionary to store a*a for all a < sqrt(c), and check c - a*a in dictionary or not
A better solution would be using the general format of Fermat's theory:
https://en.wikipedia.org/wiki/Sum_of_two_squares_theorem
"""
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        mark = int(c ** 0.5)
        squas = {}
        for i in range(mark+1):
            squas[i * i] = i
        for i in squas:
            if c - i in squas:
                return True
        return False
