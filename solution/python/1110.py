"""
@difficulty: medium
@tags: tree, dfs
@notes: DFS with stack, saves valid children to result only when current node should be deleted.
"""
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        if not root:
            return []
        dummy = TreeNode(0)
        dummy.left = root
        res = []
        stack = [dummy]
        toDeleteSet = set(to_delete)
        while stack:
            peek = stack.pop()
            if peek.right:
                stack.append(peek.right)
                if peek.right.val in toDeleteSet:
                    peek.right = None
            if peek.left:
                stack.append(peek.left)
                if peek.left.val in toDeleteSet:
                    peek.left = None
            if peek.val in toDeleteSet:
                res.extend(filter(lambda x: x is not None and x.val not in toDeleteSet, [peek.left, peek.right]))
        return res if root.val in toDeleteSet else [root] + res
