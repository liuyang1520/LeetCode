"""
@difficulty: medium
@tags: BST
@notes: BST -> list -> Balanced BST
"""
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []
        def bstToList(root):
            if not root:
                return
            bstToList(root.left)
            values.append(root.val)
            bstToList(root.right)
        def listToBalancedBst(values):
            if not values:
                return None
            mid = len(values) // 2
            root = TreeNode(values[mid])
            left = listToBalancedBst(values[: mid])
            right = listToBalancedBst(values[mid + 1: ])
            root.left = left
            root.right = right
            return root
        bstToList(root)
        return listToBalancedBst(values)
