# Recursive solution.
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


# Iterative solution. Use a list to record all visited node.
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack = [root]
        res = []
        visited = []
        while stack:
            peek = stack[-1]
            if peek.left and (peek.left not in visited):
                stack.append(peek.left)
            else:
                currentNode = stack.pop()
                visited.append(currentNode)
                res += [currentNode.val]
                if currentNode.right:
                    stack.append(currentNode.right)
        return res


# Iterative solution. To avoid infinite loops, use right child tree to jump it. Very tricky.
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack = []
        res = []
        while root != None or stack:
            if root != None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

