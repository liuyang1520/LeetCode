"""
Seperate into left, xxx, right.
"""
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m >= n:
            return head
        dummy = ListNode(0)
        dummyHead = ListNode(0)
        dummyHead.next = head
        # get left segment end node
        left, count = dummyHead, 1
        while left and count <= m-1:
            left = left.next
            count += 1
        # get right segment head node
        right, count = dummyHead, 1
        while right and count <= n:
            right = right.next
            count += 1
        right.next, right = None, right.next
        dummy.next = left.next
        # reverse the linked list from m to n
        prev, end = None, left.next
        while dummy.next:
            temp = dummy.next.next
            dummy.next.next = prev
            prev = dummy.next
            dummy.next = temp
        left.next = prev
        end.next = right
        return dummyHead.next