# Can add dummy node to avoid edge cases.
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head
        start = head.next
        while head and head.next:
            temp = head.next.next
            head.next.next = head
            if temp and (not temp.next):
                head.next = temp
            elif not temp:
                head.next = None
            else:
                head.next = temp.next
            head = temp
        return start