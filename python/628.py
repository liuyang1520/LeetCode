"""
Sort then find the largest / smallest positive and negative values.
Actually there is no need to sort, can iterate all numbers and only compare those possible values.
"""
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            return reduce(lambda x, y: x * y, nums)

        positives = sorted(filter(lambda x: x >= 0, nums))
        negatives = sorted(filter(lambda x: x < 0, nums))

        if not negatives:
            return positives[-1] * positives[-2] * positives[-3]
        if not positives:
            return negatives[-1] * negatives[-2] * negatives[-3]
        if len(positives) == 1:
            return positives[0] * negatives[0] * negatives[1]
        if len(positives) == 2:
            return negatives[0] * negatives[1] * positives[-1]
        return max(positives[-1] * positives[-2] * positives[-3],
                   negatives[0] * negatives[1] * positives[-1])
