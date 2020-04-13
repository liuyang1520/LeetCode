"""
@difficulty: medium
@tags: recursion
@notes: Recursively go through all nodes, if left and right and truncated and root value is target, truncate whole branch.
"""
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        return self.helper(root, target)
        
    def helper(self, root, target):
        if not root:
            return None
        left = self.helper(root.left, target)
        right = self.helper(root.right, target)
        if left == right == None and root.val == target:
            return None
        root.left = left
        root.right = right
        return root
