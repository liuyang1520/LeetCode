# Can be implemented in binary search with worst case O(n).
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        try:
            return bool(nums.index(target) + 1)
        except:
            return False