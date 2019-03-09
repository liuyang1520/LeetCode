# My mass solution...
# 0, 1, 2, 3, 4, ..., k, k + 1, k + 2, ....
# 1) Test whether first k + 1 elements have duplicate numbers.
# 2) If not, test (1, k + 1), (2, k + 1, k + 2) ...
# 3) Start from k + 1 and do the things again.
# O(n + k^2) time, and O(k) hashmap space.
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        if k >= len(nums):
            return len(set(nums)) != len(nums)
        start = 0
        end = len(nums) - 1
        while start + k < end:
            if len(set(nums[start: start+k+1])) != k + 1:
                return True
            j = 1
            i = start + j
            while i <= start + k and i + k <= end:
                for s in range(1, j + 1):
                    print start, k, s
                    if nums[i] == nums[start + k + s]:
                        return True
                j += 1
                i = start + j
            start += k + 1
        if start < end:
            return len(set(nums[start:])) != len(nums[start:])
        return False


# Elegant solution, use a dictionary (hashmap) store the position values, and keep test the distances of existing values.
# O(n) time, and O(n) hashmap space.
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        posDict = {}
        for i in range(len(nums)):
            if nums[i] not in posDict:
                posDict[nums[i]] = i
            else:
                if i - posDict[nums[i]] <= k:
                    return True
                else:
                    posDict[nums[i]] = i
        return False