class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for row in A:
            res.append(map(lambda x: [1,0][x], row[::-1]))
        return res
