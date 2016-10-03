"""
Use merge sort to sort the linked list.
Note: the solution below changes the original linked list.
"""
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = fast = head
        temp = ListNode(0)
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next = None
        head1 = self.sortList(head)
        head2 = self.sortList(slow)
        return self.merge(head1, head2)
        
    def merge(self, head1, head2):
        head = ListNode(0)
        tempHead = head
        while head1 and head2:
            if head1.val < head2.val:
                tempHead.next = head1
                head1 = head1.next
            else:
                tempHead.next = head2
                head2 = head2.next
            tempHead = tempHead.next
        if head1:
            tempHead.next = head1
        if head2:
            tempHead.next = head2
        return head.next