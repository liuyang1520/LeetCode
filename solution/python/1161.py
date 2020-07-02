"""
@difficulty: medium
@tags: DFS
@notes: Iterate the whole tree to get the sums for each level, then sort the results to get the proper answer.
"""
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        from collections import defaultdict
        stats = defaultdict(int)
        def dfs(root, level):
            if not root:
                return
            stats[level] += root.val
            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)
        dfs(root, 1)
        return sorted(stats.items(), key = lambda x: [x[1], -x[0]], reverse = True)[0][0]
