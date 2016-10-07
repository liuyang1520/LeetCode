"""
Very tricky solution.
Use inorder traversal with prev pointer.
Since prev always points to the previous node, it is not valid when current node is smaller than prev.
Use node1, node2 to update the value.
"""
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.node1, self.node2 = None, None
        self.prev = None
        self.recoverTreeHelper(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
        
        
    def recoverTreeHelper(self, root):
        if root:
            self.recoverTreeHelper(root.left)
            if self.prev and self.prev.val > root.val:
                self.node2 = root
                if not self.node1:
                    self.node1 = self.prev
            self.prev = root
            self.recoverTreeHelper(root.right)