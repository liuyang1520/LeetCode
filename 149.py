"""
1. For each point, we only need to calculate the most common slope value
from other points (actually we can omit the points which has already been
counted). Using a hash table can make this happen in O(n^2).

2. In order to pass the test case like this:
[10000000001, 10000000000], [10000000002, 10000000001]
we need to keep the precision of division.
Fraction module in Python got TLE.
So have to write greatest common divisor method.

3. Note the case like this:
[0, 0], [1, 1], [-1, -1].
Use a pair of int for hash need to handle the negatives.
"""
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def getSlope(p1, p2):
            if p1.x == p2.x: return float('inf')
            dx, dy = p2.x - p1.x, p2.y - p1.y
            if dx == 0 or dy == 0:
                return (0, 0)
            d = gcd(abs(dx), abs(dy)) * dx / abs(dx)
            return (dx/d, dy/d)
        
        def gcd(a, b):
            if a > b: a, b = b, a
            r = b % a
            if r == 0:
                return a
            else:
                return gcd(r, a)
        
        res = 0
        for i in range(len(points)):
            countDict, overlap = {}, 0
            p1 = points[i]
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p1.x == p2.x and p1.y == p2.y:
                    overlap += 1
                else:
                    k = getSlope(p1, p2)
                    if k not in countDict:
                        countDict[k] = 1
                    else:
                        countDict[k] += 1
            res = max(max(countDict.values()+[0]) + overlap + 1, res)
        return res