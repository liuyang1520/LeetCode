"""
Sol 1: For each number, sum it with another one O(n^2/2) = O(n^2)
Sol 2: Sort the list, then use two pointer pointing the start and end,
        if start + end > target: end--
                       < target: start++
                       = target: return
        O(nlogn)
Sol 3: Hashmap, push numbers into hashmap, then search in hash, O(n)
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in dict:
                return (dict[target - x], i)
            dict[x] = i