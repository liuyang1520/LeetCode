# Merge the larger linked list into the smaller one. Creating a new linked list may be a better alternative solution
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        first = l1 if l1.val <= l2.val else l2
        second = l1 if l1.val > l2.val else l2
        root = first
        while first:
            if not first.next:
                first.next = second
                first = None
            elif not second:
                first = None
            elif first.val <= second.val <= first.next.val:
                pointer1 = first.next
                pointer2 = second.next
                first.next = second
                second.next = pointer1
                first = first.next
                second = pointer2
            else:
                first = first.next
        return root