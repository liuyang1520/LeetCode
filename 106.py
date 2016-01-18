# Exceed Memory Limit solution.
# inorder:   4, 2, 5, 6, 1, 3
# postorder: 4, 6, 5, 2, 3, 1
# Find last element in postorder (1), find it in inorder list. Then split inorder and postorder lists accordingly.
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not len(inorder):
            return None
        root = TreeNode(postorder[-1])
        pos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:pos], postorder[:pos])
        root.right = self.buildTree(inorder[pos + 1:], postorder[pos: -1])
        return root

# An improvement was made to save memory usage. Only use the start and end pointers instead of passing the whole lists.
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inorder = inorder
        self.postorder = postorder
        return self.buildTreeHelp(0, len(inorder) - 1, 0, len(inorder) - 1)
        
    def buildTreeHelp(self, start1, end1, start2, end2):
        if start1 > end1:
            return None
        root = TreeNode(self.postorder[end2])
        pos = self.inorder[start1: end1 + 1].index(self.postorder[end2])
        root.left = self.buildTreeHelp(start1, start1 + pos - 1, start2, start2 + pos - 1)
        root.right = self.buildTreeHelp(start1 + pos + 1, end1, start2 + pos, end2 - 1)
        return root