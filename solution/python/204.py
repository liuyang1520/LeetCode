# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        primes = [1] * n
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                j = i
                while i * j < n:
                    primes[i * j] = 0
                    j += 1
        return sum(primes) - 2