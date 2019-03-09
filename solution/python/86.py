# Create two pointers to seperate list nodes into two linked list.
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = ListNode(0)
        newHead = small
        large = ListNode(0)
        newHalfHead = large
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        small.next = newHalfHead.next
        large.next = None
        return newHead.next