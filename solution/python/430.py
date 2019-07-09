"""
@difficulty: medium
@tags: dfs
@notes: The helper returns start and end of transformed double linked list.
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def helper(head):
            _start, _end = head, None
            while head:
                if head.child:
                    temp = head.next
                    start, end = helper(head.child)
                    head.next = start
                    head.child = None
                    head.next.prev = head
                    end.next = temp
                    if temp:
                        temp.prev = end
                    _end = end
                    head = end.next
                else:
                    _end = head
                    head = head.next
                if not _end.next:
                    return [_start, _end]
            return [_start, _end]
        head, _ = helper(head)
        return head
