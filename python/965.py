"""
@difficulty: easy
@tags: stack, dfs, tree
@notes: DFS on the tree compare node values, terminate immediately wheneven values are different.
"""
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [root]
        while stack:
            temp = stack.pop()
            if temp.right:
                if temp.val == temp.right.val:
                    stack.append(temp.right)
                else:
                    return False
            if temp.left:
                if temp.val == temp.left.val:
                    stack.append(temp.left)
                else:
                    return False
        return True
