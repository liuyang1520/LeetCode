"""
Use a dictionary to memorize the result would improve the speed
"""
class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N == 1:
            return [TreeNode(0)]
        res = []
        for i in range(1, N - 1, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N-1-i):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res
