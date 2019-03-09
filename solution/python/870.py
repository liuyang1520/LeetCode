"""
Sort + binary search
"""
class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort(reverse=True)
        res = []
        for e in B:
            flag = False
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) / 2
                if A[mid] > e and mid + 1 < len(A) and A[mid+1] <= e:
                    flag = True
                    res.append(A[mid])
                    A.pop(mid)
                    break
                elif A[mid] <= e:
                    right = mid - 1
                else:
                    left = mid + 1
            if not flag:
                res.append(A.pop())
        return res
