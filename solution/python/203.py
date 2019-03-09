# Create a dummy node right previous to the head, use prev and head these two points to update the list.
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next