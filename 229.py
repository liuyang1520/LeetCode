# https://leetcode.com/discuss/43248/boyer-moore-majority-vote-algorithm-and-my-elaboration
# An variation of Moore Vote Algorithm.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count1 = count2 = 0
        major1 = major2 = None
        for i in nums:
            if major1 == i:
                count1 += 1
            elif major2 == i:
                count2 += 1
            elif count1 == 0:
                major1 = i
                count1 = 1
            elif count2 == 0:
                major2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        return [i for i in [major1, major2] if nums.count(i) > len(nums) / 3]