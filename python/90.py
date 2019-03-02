# Use set() to get rid of duplicate results. Note set() only works for lists of tuples.
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        total = 2 ** (len(nums))
        nums.sort()
        for i in range(total):
            choice = []
            binExp = ("{:0"+str(len(nums))+"b}").format(i)  # or bin(i)[2:]
            for j in range(len(binExp)):
                if binExp[j] == "1":
                    choice.append(nums[j])
            res.append(tuple(choice))
        res = set(res)
        return list(res)