"""
Sort the nums, then iterate the nums copy to change rank.
"""
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        numsRank = list(enumerate(nums))
        numsRank.sort(key = lambda x: x[1], reverse = True)
        numsCopy = nums[::]
        for i in range(len(numsRank)):
            if i == 0:
                numsCopy[numsRank[i][0]] = "Gold Medal"
            elif i == 1:
                numsCopy[numsRank[i][0]] = "Silver Medal"
            elif i == 2:
                numsCopy[numsRank[i][0]] = "Bronze Medal"
            else:
                numsCopy[numsRank[i][0]] = str(i + 1)
        return numsCopy