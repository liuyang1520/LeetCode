"""
@difficulty: easy
@tags: BFS
@notes: Run a BFS on the tree, exclude the leaves on the same parent.
"""
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        queue = [root]
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                if node.left and node.right and sorted([node.left.val, node.right.val]) == sorted([x, y]):
                    return False
            values = map(lambda x: x.val, temp)
            if x in values and y in values:
                return True
            queue = temp
        return False
        
