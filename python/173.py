# Push left children in a stack. Push right child when poping elements.
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushChild(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        if node.right:
            self.pushChild(node.right)
        return node.val
        
    def pushChild(self, node):
        while node:
            self.stack.append(node)
            node = node.left