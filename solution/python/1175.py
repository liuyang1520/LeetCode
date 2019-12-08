"""
@difficulty: easy
@tags: math
@notes: Count the number of primes, then do a factorial on the count.
"""
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def countPrime(n):
            count = 0
            for i in range(2, n+1):
                isPrime = True
                for j in range(2, int(i**0.5)+1):
                    if i % j == 0:
                        isPrime = False
                        break
                if isPrime:
                    count += 1
            return count
        def factorial(n):
            # Can be replaced by math.factorial or
            # functools.reduce
            res = 1
            for i in range(1, n+1):
                res *= i
            return res
        primeCount = countPrime(n)
        nonPrimeCount = n - primeCount
        print(primeCount)
        return (factorial(primeCount) * factorial(nonPrimeCount)) % int(1e9 + 7)
