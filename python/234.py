'''
1) Find mid node;
2) Reverse second half;
3) Compare.
All cases:
None, 1, 1->2, 1->2->3, 1->2->3->4
'''
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        # Get mid node of list
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        # Reverse second half
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        # Determine palindrome or not
        head2 = prev
        while head and head2:
            if head.val != head2.val:
                return False
            else:
                head, head2 = head.next, head2.next
        return True