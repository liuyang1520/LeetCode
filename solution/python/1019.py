"""
@difficulty: medium
@tags: stack, linked list
@notes: Similar to #503, use a stack to store previous values.
"""
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res, stack = [], []
        while head:
            res.append(0)
            val = head.val
            while stack and stack[-1][1] < val:
                index, _ = stack.pop()
                res[index] = val
            stack.append([len(res) - 1, val])
            head = head.next
        return res
