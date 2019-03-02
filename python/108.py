# Recursive solution.
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        left = 0
        right = len(nums)
        mid = (left + right) / 2
        root = TreeNode(nums[mid])
        if mid > left:
            root.left = self.sortedArrayToBST(nums[left: mid])
        if right > mid + 1:
            root.right = self.sortedArrayToBST(nums[mid + 1: right])
        return root