"""
@difficulty: medium
@tags: DFS
@notes: Traverse the trees then sort, or traverse in-orderly with 2 pointers.
"""
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root, values):
            if not root:
                return values
            values.append(root.val)
            dfs(root.left, values)
            dfs(root.right, values)
            return values
        values1 = dfs(root1, [])
        values2 = dfs(root2, [])
        return sorted(values1 + values2)
