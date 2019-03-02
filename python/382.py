"""
1. classic solution with length
2. Reservoir Sampling
"""
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.length = 0
        while head:
            self.length += 1
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        steps = random.randint(0, self.length - 1)
        temp = self.head
        while steps:
            temp = temp.next
            steps -= 1
        return temp.val


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        from random import randint
        count = 0
        res = self.head
        temp = res
        while temp:
            if randint(0, count) == 0:
                res = temp
            count += 1
            temp = temp.next
        return res.val