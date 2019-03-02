"""
1. subset sum, 2D-DP, 2752 ms
2. subset sum, 1D-DP, 1009 ms
3. subset sum, use a set to store the sum values
4. bitset (C++), http://www.cnblogs.com/grandyang/p/5951422.html
"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2:
            return False
        total = total / 2
        dp = [[False]*(total+1) for i in range(len(nums)+1)]
        for i in range(len(dp)):
            dp[i][0] = True
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i-1][j]
                if not dp[i][j] and nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]]
        return dp[-1][-1]


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2:
            return False
        total = total / 2
        dp = [False] * (total+1)
        dp[0] = True
        for num in nums:
            # Note, must be descenting order, counter-example: [1, 2, 5] -> [1, 2, 3, 4], when calculate 4
            for i in range(len(dp)-1, num-1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[-1]


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2:
            return False
        total = total / 2
        sumSet = set([0])
        for i in nums:
            for j in sumSet.copy():
                sumSet.add(i + j)
        return total in sumSet


class Solution {
public:
    bool canPartition(vector<int>& nums) {
        bitset<5001> bits(1);
        int sum = accumulate(nums.begin(), nums.end(), 0);
        for (int num : nums) bits |= bits << num;
        return (sum % 2 == 0) && bits[sum >> 1];
    }
};