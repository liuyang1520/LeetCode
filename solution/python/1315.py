"""
@difficulty: medium
@tags: BFS
@notes: Use BFS to iterate the tree, need to record the grandparent value during the process.
"""
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = [[root, []]]
        res = 0
        while queue:
            node, parents = queue.pop(0)
            if not node:
                continue
            if len(parents) == 2 and parents[0] % 2 == 0:
                res += node.val
            if len(parents) == 2:
                parents.pop(0)
            parents.append(node.val)
            if node.left:
                queue.append([node.left, parents[:]])
            if node.right:
                queue.append([node.right, parents[:]])
        return res
