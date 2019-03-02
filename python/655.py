"""
Use the height and offset to calculate the position of the char to change, do it recursively
"""
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        self.maxHeight = self.getHeight(root)
        self.results = [[''] * (2 ** self.maxHeight - 1) for i in range(self.maxHeight)]
        self.helper(root, 0, self.maxHeight)
        return self.results


    def helper(self, root, offset, height):
        if not root: return
        index = self.maxHeight - height
        mid = 2 ** (self.maxHeight - 1) - 1
        self.results[index][mid + offset] = str(root.val)
        if root.left: self.helper(root.left, offset - 2 ** (height-2), height - 1)
        if root.right: self.helper(root.right, offset + 2 ** (height-2), height - 1)


    def getHeight(self, root):
        if not root: return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
