"""
@difficulty: easy
@tags: BFS
@notes: This solution uses BFS. DFS or recursion should both work.
"""
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [(root, str(root.val))]
        res = []
        while queue:
            node, values = queue.pop(0)
            if node.left:
                queue.append((node.left, values + str(node.left.val)))
            if node.right:
                queue.append((node.right, values + str(node.right.val)))
            if not node.left and not node.right:
                res.append(values)
        return sum(map(lambda x: int(x, 2), res))
