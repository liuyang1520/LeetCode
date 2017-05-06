"""
DFS, save the left, right subsum values for reuse, or will get TLE
"""
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.subsum(root)
        return self.res

    def subsum(self, root):
        if not root:
            return 0
        left, right = self.subsum(root.left), self.subsum(root.right)
        self.res += abs(left - right)
        return left + right + root.val
