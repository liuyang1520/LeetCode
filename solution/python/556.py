"""
Note the list copy:
1. b = a[:]
2. b = list(a)
"""
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums: return nums
        nums_r, nums_c = len(nums), len(nums[0])
        if nums_r * nums_c != r * c: return nums

        new_nums = []
        counter, temp_row = 0, []
        for row in nums:
            for num in row:
                if counter < c:
                    temp_row.append(num)
                    counter += 1
                if counter == c:
                    new_nums.append(temp_row[:])
                    counter, temp_row = 0, []
        return new_nums
