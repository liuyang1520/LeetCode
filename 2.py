# Convert Linked List to numbers then do the summation.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getNumFromLL(root):
            if not root: return 0
            num = ""
            while root:
                num += str(root.val)
                root = root.next
            return int(num[::-1])
            
        num1, num2 = getNumFromLL(l1), getNumFromLL(l2)
        res = str(num1 + num2)[::-1]
        root = ListNode(int(res[0]))
        head = root
        for i in range(1, len(res)):
            root.next = ListNode(int(res[i]))
            root = root.next
        return head