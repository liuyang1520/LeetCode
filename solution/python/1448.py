"""
@difficulty: medium
@tags: DFS
@notes: Iterate all nodes, compare its value with the max values from the path.
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, prevMax):
            if not node:
                return
            if node.val >= prevMax:
                self.goodNodes += 1
            prevMax = max(node.val, prevMax)
            if node.left:
                dfs(node.left, prevMax)
            if node.right:
                dfs(node.right, prevMax)
        self.goodNodes = 0
        dfs(root, -float('inf'))
        return self.goodNodes
