# 1. Find the mid-node of the chain, using fast-slow-pointer technique;
# 2. Reverse the right half;
# 3. Join the two linked lists.
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        res = head
        if head:
            # Find mid node
            slow = fast = head
            while fast and fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            mid = slow.next
            if slow != fast:
                slow.next = None
                # Reverse the linked list from mid to last
                prev = None
                while mid:
                    temp = mid.next
                    mid.next = prev
                    prev = mid
                    mid = temp
                # Combine the two lists
                while prev:
                    temp = prev.next
                    prev.next = head.next
                    head.next = prev
                    head = prev.next
                    prev = temp
        head = res