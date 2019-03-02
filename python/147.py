# Use a dummy ListNode for convenience.
# Improvement: first compare the node to right-most node, if larger, insert it directly. Best case O(n), worst case O(n^2).
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        newHead = ListNode(-1)
        newHead.next = ListNode(head.val)
        while head.next:
            head = head.next
            current = newHead.next
            prev = newHead
            while current and current.val < head.val:
                prev = current
                current = current.next
            temp = prev.next
            prev.next = ListNode(head.val)
            prev.next.next = temp
        return newHead.next