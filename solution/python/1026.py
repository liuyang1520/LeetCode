"""
@difficulty: medium
@tags: tree
@notes: Compare the min, max values recursively, or pass the min, max values to branches.
"""
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def helper(root):
            if not root:
                return [float('inf'), -float('inf')]
            if hasattr(root, 'min'):
                return [root.min, root.max]
            minVal, maxVal = root.val, root.val
            if root.left:
                lmin, lmax = helper(root.left)
                minVal, maxVal = min(minVal, lmin), max(maxVal, lmax)
                self.res = max(self.res, abs(root.val - lmin), abs(root.val - lmax))
            if root.right:
                rmin, rmax = helper(root.right)
                minVal, maxVal = min(minVal, rmin), max(maxVal, rmax)
                self.res = max(self.res, abs(root.val - rmin), abs(root.val - rmax))
            root.min = minVal
            root.max = maxVal
            return [minVal, maxVal]
        helper(root)
        return self.res
