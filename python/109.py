# Recursively attaching the left and right sub-list to the root (mid) TreeNode.
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # Convert linked list to list.
        self.nums = []
        while head:
            self.nums.append(head.val)
            head = head.next
        # Convert list to BST.
        return self.listToBST(0, len(self.nums) - 1)
        
        
    def listToBST(self, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        root = TreeNode(self.nums[mid])
        root.left = self.listToBST(start, mid - 1)
        root.right = self.listToBST(mid + 1, end)
        return root