"""
@difficulty: medium
@tags: DFS, tree
@notes: Traverse the whole tree with DFS to find the minimum string.
"""
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.minStr = "{"
        self.dfs(root, "")
        return self.minStr
        
    def dfs(self, root, string):
        if not root:
            return string
        string = chr(root.val + 97) + string
        if root.left:
            self.dfs(root.left, string)
        if root.right:
            self.dfs(root.right, string)
        if not root.left and not root.right:
            self.minStr = min(self.minStr, string)
