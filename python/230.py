# Use in-order traversal to get the result.
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        nums = []
        flag = 0
        while (root is not None or stack) and (flag < k):
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                nums.append(root.val)
                flag += 1
                root = root.right
        return nums[-1]