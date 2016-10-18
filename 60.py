"""
1. DFS, TLE
2. Calculate how many conditions exist for each starting number
For example, n = 4, k = 5
seq = [1,2,3,4], k / (3*2*1) = 0, so start at "1", the k % (3*2*1) = 5th;
seq = [2,3,4], k / (2*1) = 2 ...... 1, so start at "4", the 1th;
seq = [2,3], 1th is "23"
get "1423"
"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.count = 0
        self.n, self.k = n, k
        self.res = ""
        self.dfs("")
        return self.res
    
    def dfs(self, seq):
        if len(seq) == self.n:
            self.count += 1
            if self.count == self.k:
                self.res = seq
            return
        for i in range(1, self.n+1):
            if str(i) not in seq:
                self.dfs(seq + str(i))


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        
        def factor(f):
            res = 1
            for i in range(1, f+1):
                res *= i
            return res
            
        def getPermutationHelper(seq, k):
            n = len(seq)
            if k == 0:
                res.append(seq[::-1])
                return
            if n == 1:
                res.append(seq)
                return
            count = factor(n-1)
            div, remainer = int(math.ceil(float(k) / count)), k % count
            res.append(seq[div - 1])
            getPermutationHelper(seq[:(div - 1)] + seq[div:], remainer)
            
        res = []
        getPermutationHelper("".join(map(str, range(1, n+1))), k)
        return "".join(res)