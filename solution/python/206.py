# Iterative solution.
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        node = head.next
        head.next = None
        while node:
            temp = node.next
            node.next = head
            head = node
            node = temp
        return head