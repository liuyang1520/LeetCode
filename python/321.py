"""
1. Get max nums from each list
2. Merge them in a single list
3. Iterate all conditions above
Note:
1. range(max(0, k - len(nums2)), min(len(nums1), k) + 1), for k > len(nums1) or k > len(nums2)
2. if res1[p:] > res2[q:], for [6, 0], [6, 7], need to compare the rest elements.
3. The merge part can be replaced with:
    res = max(res, [max(res1, res2).pop(0) for _ in xrange(k)])
"""
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def findMaxNumber(nums, k):
            res = []
            for i in range(len(nums)):
                while res and res[-1] < nums[i] and len(nums) - i - 1 >= k - len(res):
                    res.pop()
                if len(res) < k:
                    res.append(nums[i])
            return res
        
        res = []
        for i in range(max(0, k - len(nums2)), min(len(nums1), k) + 1):
            res1 = findMaxNumber(nums1, i)
            res2 = findMaxNumber(nums2, k - i)
            p = q = 0
            temp = []
            while p < len(res1) and q < len(res2):
                if res1[p:] > res2[q:]:
                    temp.append(res1[p])
                    p += 1
                else:
                    temp.append(res2[q])
                    q += 1
            if p == len(res1):
                temp.extend(res2[q:])
            else:
                temp.extend(res1[p:])
            res = max(res, temp)
        return res