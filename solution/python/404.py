"""
Recursive solution
"""
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if root:
            self.sumOfLeftLeavesHelper(root)
        return self.res
        
    def sumOfLeftLeavesHelper(self, root):
        if root.left:
            if not root.left.left and not root.left.right:
                self.res += root.left.val
            else:
                self.sumOfLeftLeavesHelper(root.left)
        if root.right:
            self.sumOfLeftLeavesHelper(root.right)