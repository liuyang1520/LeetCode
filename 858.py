"""
https://leetcode.com/problems/mirror-reflection/solution/
"""
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        from fractions import gcd
        g = gcd(p, q)
        p = (p / g) % 2
        q = (q / g) % 2
        return 1 if p and q else 0 if p else 2
