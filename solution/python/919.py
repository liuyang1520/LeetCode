"""
Similar to a heap, keep references to all nodes
"""
class CBTInserter(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self._heap = [root]
        self.root = root
        # BFS
        queue = [root]
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    self._heap.append(node.left)
                    temp.append(node.left)
                if node.right:
                    self._heap.append(node.right)
                    temp.append(node.right)
            queue = temp

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)
        self._heap.append(node)
        lastIndex = len(self._heap) - 1
        if lastIndex % 2:
            self._heap[(lastIndex - 1) / 2].left = node
            return self._heap[(lastIndex - 1) / 2].val
        else:
            self._heap[(lastIndex - 2) / 2].right = node
            return self._heap[(lastIndex - 2) / 2].val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
