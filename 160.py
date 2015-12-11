# O(m + n). Get the length of two lists, then get into the longer list a few steps ahead.
# http://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (not headA) or (not headB):
            return None
        lengthA = lengthB = 1
        headATemp, headBTemp = headA, headB
        while headA.next:
            lengthA += 1
            headA = headA.next
        while headB.next:
            lengthB += 1
            headB = headB.next
        if lengthA > lengthB:
            for i in range(lengthA - lengthB):
                headATemp = headATemp.next
        else:
            for i in range(lengthB - lengthA):
                headBTemp = headBTemp.next
        while headATemp and headBTemp:
            if headATemp == headBTemp:
                return headATemp
            headATemp = headATemp.next
            headBTemp = headBTemp.next
        return None