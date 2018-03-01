"""
max R is 10^6 < 1024 * 1024 = 2 ^ 20
so only need the prime number dictionary smaller than 20
"""
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        count = 0
        primeSet = set([2, 3, 5, 7, 11, 13, 17, 19])
        for i in range(L, R + 1):
            if bin(i).count('1') in primeSet:
                count += 1
        return count
