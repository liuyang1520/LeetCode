"""
@difficulty: medium
@tags: DFS
@notes: DFS, store the {depth: sum}, then find the max depth.
"""
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        nodes = {}
        def dfs(root, depth = 0):
            if not root:
                return
            if depth in nodes:
                nodes[depth] += root.val
            else:
                nodes[depth] = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root)
        return nodes[max(nodes.keys())]
