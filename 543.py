"""
Resursively find the max left and right length, then update the max length
"""
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.maxLen = 0
        self.dfs(root)

        return self.maxLen
    
    def dfs(self, root):
        left = right = 0
        if root.left:
            left = self.dfs(root.left) + 1
        if root.right:
            right = self.dfs(root.right) + 1
        self.maxLen = max(left + right, self.maxLen)
        return max(left, right)