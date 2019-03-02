# Change the words to nums, and use bit operations to save time. Or will running out of time.
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        nums = []
        for i in words:
            nums.append(sum(1 << (ord(j) - ord('a')) for j in set(i)))
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if not (nums[i] & nums[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res
