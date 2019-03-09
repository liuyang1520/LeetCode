# Naive solution, use a hashtable to store the values in the window, and compare it when necessary.
# Got Time Limit Error.
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        res = []
        mapList = {'maxNum': -float('inf')}
        for i in range(k):
            if nums[i] > mapList['maxNum']:
                mapList['maxNum'] = nums[i]
            mapList[nums[i]] = mapList.get(nums[i], 0) + 1
        res += [mapList['maxNum']]
        for j in range(k, len(nums)):
            if nums[j] > mapList['maxNum']:
                mapList['maxNum'] = nums[j]
                mapList[nums[j]] = 1
                mapList[nums[j - k]] -= 1
            else:
                mapList[nums[j]] = mapList.get(nums[i], 0) + 1
                mapList[nums[j - k]] -= 1
                if mapList[mapList['maxNum']] == 0:
                    submax = nums[j]
                    for p, q in mapList.items():
                        if q > 0 and p != 'maxNum' and p > submax:
                            submax = p
                    mapList['maxNum'] = submax
            res += [mapList['maxNum']]
        return res
                    
# Deque solution.
# Deque stores index of the nums array.
# 1) pop left value if it is not in window;
# 2) pop right values until larger than new value, they are dropped and not used in the future;
# 3) add new value.
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        import collections
        dq = collections.deque()
        for i in range(len(nums)):
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res += [nums[dq[0]]]
        return res