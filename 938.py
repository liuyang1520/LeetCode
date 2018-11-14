"""
DFS
"""
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def helper(root, total):
            if not root:
                return 0
            if root.val < L:
                total += helper(root.right, 0)
            elif root.val > R:
                total += helper(root.left, 0)
            else:
                total += root.val + helper(root.left, 0) + helper(root.right, 0)
            return total
        return helper(root, 0)
