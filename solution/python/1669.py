"""
@difficulty: medium
@tags: linked list
@notes: brute force to find the left and right border then connect.
"""
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
        index = 0
        left, right = None, None
        while temp:
            if index == a - 1:
                left = temp
            if index == b + 1:
                right = temp
                break
            temp = temp.next
            index += 1
        left.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = right
        return list1
