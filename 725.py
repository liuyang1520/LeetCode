"""
1. Get the length of the Single LL;
2. Calculate the breakpoints;
3. Break Single LL into smaller parts.
"""
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        size = 0
        temp = root
        while temp:
            size += 1
            temp = temp.next
        smaller = size / k
        biggerCount = size % k
        bigger = smaller + 1 if biggerCount else smaller
        smallerCount = k - biggerCount
        results = []
        for i in [bigger] * biggerCount + [smaller] * smallerCount:
            results.append(root)
            if not root: continue
            for j in range(i-1):
                root = root.next
            temp, root.next = root.next, None
            root = temp
        return results
