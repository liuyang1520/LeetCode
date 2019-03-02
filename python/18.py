# Solution 1: n^3*log(n), 3 for loop + binary search. Time Limit Exceed.
# Solution 2: n^4 (worst case), n^2log(n) in average, store sum of two numbers in a dictionary beforehand to save time.
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        length = len(nums)
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, length):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j + 1, length):
                    if k > j + 1 and nums[k] == nums[k-1]:
                        continue
                    left = k + 1
                    right = length - 1
                    while left <= right:
                        mid = (left + right) / 2
                        temp = [nums[i], nums[j], nums[k], nums[mid]]
                        if sum(temp) == target:
                            res.append(temp)
                            break
                        elif sum(temp) > target:
                            right = mid - 1
                        else:
                            left = mid + 1
        return res


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        nums = sorted(nums)
        length = len(nums)
        pairSums = {}
        for i in range(length):
            for j in range(i + 1, length):
                pair = [i, j]
                total = nums[i] + nums[j]
                if total not in pairSums:
                    pairSums[total] = [pair]
                elif pair not in pairSums[total]:
                    pairSums[total].append(pair)
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, length):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                if target - nums[i] - nums[j] in pairSums:
                    for pair in pairSums[target - nums[i] - nums[j]]:
                        if pair[0] > j:
                            res.add((nums[i], nums[j], nums[pair[0]], nums[pair[1]]))
        return [list(i) for i in res]