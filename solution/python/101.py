# Iteratively solution.
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left = [root.left]
        right = [root.right]
        while left and right:
            leftRoot = left.pop()
            rightRoot = right.pop()
            if (leftRoot is None and rightRoot is not None) or (leftRoot is not None and rightRoot is None):
                return False
            elif leftRoot is not None and rightRoot is not None:
                if leftRoot.val != rightRoot.val:
                    return False
                else:
                    left.extend([leftRoot.left, leftRoot.right])
                    right.extend([rightRoot.right, rightRoot.left])
        return True


# Recursive solution.
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymmetricHelp(root.left, root.right)
    
    def isSymmetricHelp(self, left, right):
        if left == right == None:
            return True
        if not (left and right):
            return False
        if left.val != right.val:
            return False
        return self.isSymmetricHelp(left.left, right.right) and self.isSymmetricHelp(left.right, right.left)