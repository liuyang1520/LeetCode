"""
Slow fast pointer
"""
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = quick = head
        while quick.next:
            if quick.next:
                quick = quick.next
                slow = slow.next
                if quick.next:
                    quick = quick.next
        return slow
