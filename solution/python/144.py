# Recursive solution.
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


# Iterative solution.
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack = [root]
        res = []
        while stack:
            currentNode = stack.pop()
            res += [currentNode.val]
            if currentNode.right != None:
                stack.append(currentNode.right)
            if currentNode.left != None:
                stack.append(currentNode.left)
        return res