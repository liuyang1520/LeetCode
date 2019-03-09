"""
Recursive solution, update max in each recursive process, also return the value for last recursive call
"""
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLength = 0
        if root: self.helper(root)
        return self.maxLength

    def helper(self, root):
        leftLength, rightLength = 0, 0
        if root.left:
            if root.left.val == root.val:
                leftLength = self.helper(root.left) + 1
            else:
                self.helper(root.left)
        if root.right:
            if root.right.val == root.val:
                rightLength = self.helper(root.right) + 1
            else:
                self.helper(root.right)
        if leftLength + rightLength > self.maxLength:
            self.maxLength = leftLength + rightLength
        return max(leftLength, rightLength)
