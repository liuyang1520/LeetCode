"""
@difficulty: medium
@tags: math, misc
@notes: https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/discuss/260847/JavaC%2B%2BPython-O(S2)
"""
class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        return all(bin(i)[2:] in S for i in xrange(1, N+1))
