# Use binary to select numbers. E.g, 3 numbers, 0, 1, 2, ..., 7, the binary expressions are all subsets.
# DFS is an alternative solution.
class Solution(object):
    def subsets(self, nums):
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
            res.append(choice)
        return res