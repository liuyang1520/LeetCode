"""
Tree traversal, DFS can save time by ignoring some branches
"""
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return -1
        smallestValue = root.val
        secondSmallestValue = float('inf')
        queue = [root]
        while queue:
            temp = queue.pop(0)
            if temp.val != smallestValue and temp.val < secondSmallestValue:
                secondSmallestValue = temp.val
            if temp.left:
                queue.append(temp.left)
                queue.append(temp.right)
        if secondSmallestValue != float('inf'):
            return secondSmallestValue
        else:
            return -1
