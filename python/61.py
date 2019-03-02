# Note, k can be larger than length, so need to do k %= length
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        headcopy = head
        length = 0
        while head:
            length += 1
            tail = head
            head = head.next
        if k % length == 0:
            return headcopy
        else:
            k %= length
        head = headcopy
        for i in range(length - k - 1):
            head = head.next
        newhead = head.next
        head.next = tail.next
        tail.next = headcopy
        head = newhead
        return head