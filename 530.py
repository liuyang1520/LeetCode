"""
Use inorder traversal to get a list of values then calculate min diff.
Actually, we only need to calculate it without get the whole list.
i.e.
self.lastNode = root.val
root.val - self.lastnode
"""
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        values = self.inorderTraversal(root)
        minDiff = float('inf')
        for i in range(len(values)-1):
            minDiff = min(minDiff, values[i+1] - values[i])
        return minDiff
        
    def inorderTraversal(self, root):
        left, right = [], []
        if root.left:
            left = self.inorderTraversal(root.left)
        if root.right:
            right = self.inorderTraversal(root.right)
        return left + [root.val] + right