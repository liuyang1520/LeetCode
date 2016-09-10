# Use a hashtable to store the values and detect duplicates.
# It is sorted list, so no need to use hashtable.
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        nums = {}
        temp = head
        while head:
            if head.val not in nums:
                nums[head.val] = 1
            else:
                nums[head.val] += 1
            head = head.next
        dummy = ListNode(False)
        dummy.next = temp
        head = dummy
        while head and head.next:
            if nums[head.next.val] > 1:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next