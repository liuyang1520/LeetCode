"""
1. Try to use slow, fast pointer to solve the problem
    1	2	3	4	5	6	7	8
    1	3	2	4	5	6	7	8
    1	3	5	4	2	6	7	8
    1	3	5	7	2	6	4	8
    1	3	5	7	2	4	6	8
    
    1	2	3	4	5	6	7	8	9
    1	3	2	4	5	6	7	8	9
    1	3	5	4	2	6	7	8	9
    1	3	5	7	2	6	4	8	9
    1	3	5	7	9	6	4	8	2
    1	3	5	7	9	2	4	8	6
    1	3	5	7	9	2	4	6	8
    
    1	2	3	4	5	6
    1	3	2	4	5	6
    1	3	5	4	2	6
    1	3	5	2	4	6
think it cannot meet all conditions

2. 1->2->3: 1->3 2->.. linkedlist operation
"""
class Solution(object):
    def oddEvenList(self, head):
        if not head:
            return head
        size = 1
        slow = fast = head
        while slow.next:
            size += 1
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            elif size % 2:
                slow = slow.next
                if slow.next:
                    slow = slow.next
            elif size % 2 == 0:
                slow = slow.next
            print slow.val, fast.val
            if slow.next:
                slow.val, fast.val = fast.val, slow.val
        return head

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        odd = head
        even = evenHead = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head