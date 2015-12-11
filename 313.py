# Find solution here http://bookshadow.com/weblog/2015/12/03/leetcode-super-ugly-number/.
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, primes)) # map(gen, primes) is a list of generators. heapq.merge take these generators and sort them when next calls.
        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]: # avoid duplicates. i.e., 2*7 = 7*2
                uglies.append(ugly)
        return uglies[-1]