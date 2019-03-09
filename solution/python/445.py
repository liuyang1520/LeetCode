"""
Linked List -> String -> Int -> Linked List
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str1, str2 = '', ''
        while l1:
            str1 = str1 + str(l1.val)
            l1 = l1.next
        while l2:
            str2 = str2 + str(l2.val)
            l2 = l2.next
        res = str(int(str1) + int(str2))
        root = None
        for i in res[::-1]:
            temp = ListNode(int(i))
            temp.next = root
            root = temp
        return root
