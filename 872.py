"""
DFS
"""
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.result = []
        self.dfs(root1)
        temp = self.result[:]
        self.result = []
        self.dfs(root2)
        return temp == self.result
        
    def dfs(self, root):
        if not root:
            return
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)
        if not root.left and not root.right:
            self.result.append(root.val)
