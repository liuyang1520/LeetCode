# Use a heap to store the head of each linked list, and pop the smallest one

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        heap = []
        pos = ListNode(0)
        head = pos
        for i in lists:
            if i:
                heapq.heappush(heap, (i.val, i))
        while heap:
            cur = heapq.heappop(heap)
            pos.next = ListNode(cur[0])
            pos = pos.next
            if cur[1].next:
                heapq.heappush(heap, (cur[1].next.val, cur[1].next))
        return head.next