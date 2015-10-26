# Recursive solution for Maximum Depth of Binary Tree.
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            rtype = 0
        elif root.left == None and root.right == None:
            rtype = 1
        elif root.left == None:
            rtype = self.maxDepth(root.right) + 1
        elif root.right == None:
            rtype = self.maxDepth(root.left) + 1
        else:
            rtype = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return rtype

# A simple version of recursive solution
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            rtype = 0
        else:
            rtype = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return rtype


# Use a stack (list) to store the depth of current path, and output the max depth.
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        trace = []
        if root == None:
            return 0
        stack.append(root)
        trace.append(1)
        maxDepth = 0
        while len(stack) > 0:
            currentNode = stack.pop()
            depth = trace.pop()
            maxDepth = max(maxDepth, depth)
            if currentNode.left != None:
                stack.append(currentNode.left)
                trace.append(depth + 1)
            if currentNode.right != None:
                stack.append(currentNode.right)
                trace.append(depth + 1)
        return maxDepth


# Use a stack (list) to trace the path, this method can output the max path as well as the max depth.
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        trace = []
        if root == None:
            return 0
        stack.append(root)
        maxDepth = 0
        while len(stack) > 0:
            currentNode = stack[-1]
            if len(trace) > 0 and trace[-1] == currentNode:
                maxDepth = max(maxDepth, len(trace))
                stack.pop()
                trace.pop()
            else:
                trace.append(stack[-1])
                if currentNode.left != None:
                    stack.append(currentNode.left)
                if currentNode.right != None:
                    stack.append(currentNode.right)
        return maxDepth