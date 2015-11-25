# Slow and Fast pointers.
# When slow and fast meet somewhere in the cycle, use another pointer move from the head to meet slow.
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next and head.next.next):
            return None
        slow = head.next
        fast = head.next.next
        while slow != fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if not (fast.next and fast.next.next):
            return None
        init = head
        while slow != init and slow.next:
            slow = slow.next
            init = init.next
        return init