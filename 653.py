"""
Note: k - i != i, a number only shows once in the BST
"""
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.nodeSet = set()
        self.setupNodeSet(root)
        for i in self.nodeSet:
            if k - i != i and k - i in self.nodeSet:
                return True
        return False

    def setupNodeSet(self, root):
        self.nodeSet.add(root.val)
        if root.left:
            self.setupNodeSet(root.left)
        if root.right:
            self.setupNodeSet(root.right)
