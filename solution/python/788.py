"""
All digits must be valid, if there is any good number, then the number is good
"""
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        validNumbers = set([0, 1, 8, 2, 5, 6, 9])
        goodNumbers = set([2, 5, 6, 9])
        count = 0
        for i in range(1, N+1):
            numberStr = str(i)
            if any([int(j) not in validNumbers for j in numberStr]):
                continue
            if any([int(j) in goodNumbers for j in numberStr]):
                count += 1
        return count
