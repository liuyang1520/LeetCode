"""
Use a set to accelerate
Use a prev value to tell whether the link is broken
"""
class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        setG = set(G)
        count = 0
        prev = None
        while head:
            if head.val in setG:
                if prev is None:
                    count += 1
                    prev = head.val
            else:
                prev = None
            head = head.next
        return count
