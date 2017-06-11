"""
No need to perform the operations actually.
Note:
1. the first element is already added by 1
2. the largest the area is the overlapping area containing the first element
"""
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        x_min = min(i[0] for i in ops)
        y_min = min(i[1] for i in ops)
        return x_min * y_min
