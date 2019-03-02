# Use a list store all nodes, thus only one pass is needed.
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodeList = [ListNode(0)]
        nodeList[0].next = head
        while head:
            nodeList.append(head)
            head = head.next
        nodeList[-n-1].next = nodeList[-n].next
        return nodeList[0].next


# Two pointer solution.
# Fast pointer moves n steps in advance, slow pointer starts from the head. When fast reaches end, slow points to the removed element.
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        fp, lp = dummy, dummy
        while n > 0:
            fp = fp.next
            n -= 1
        while fp.next:
            lp = lp.next
            fp = fp.next
        lp.next = lp.next.next
        return dummy.next