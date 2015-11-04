# BFS solution, connecting the nodes in each level.
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return None
        queue = [root]
        depth = 1
        while queue:
            for i in range(depth):
                currentNode = queue.pop(0)
                if i != depth - 1:
                    currentNode.next = queue[0]
                else:
                    currentNode.next = None
                if currentNode.left:
                    queue.append(currentNode.left)
                    queue.append(currentNode.right)
            depth = depth * 2


# Recursive solution. Use node.next to connect 5, 6.
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root == None:
            return None
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None
        self.connect(root.left)
        self.connect(root.right)


# O(1) space solution. Use node.next as a linked list, performing traversals both horizentally and vertically.
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root == None:
            return None
        while root.left:
            temp = root
            while root:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
                else:
                    root.right.next = None
                root = root.next
            root = temp.left