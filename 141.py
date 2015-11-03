# Has to use a set or dictionary instead of list for tracing, since the "x in set" is much faster than "x in list".
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        trace = set()
        while head:
            trace.add(head)
            head = head.next
            if head in trace:
                return True
        return False


# Use two pointers, one slow and one fast, if they meet somewhere, then the linked list has a cycle.
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False