"""
Update level by level, need to store in the temp result like BFS queues
"""
class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        sums = A[0][:]
        for i in range(1, len(A)):
            nums = A[i]
            temp = sums[:]
            for j, value in enumerate(nums):
                left, cur, right = max(0, j-1), j, min(j+1, len(nums)-1)
                temp[j] = min(sums[left], sums[cur], sums[right]) + value
            sums = temp
        return min(sums)
