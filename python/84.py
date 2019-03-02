# An interesting problem!
# Using stack for tracing the height values in heights.
# 1) When new value is larger than peak, append it;
# 2) When new value is equal to peak, ignore it (keep the peak is enough, since the index value already counts new value in);
# 3) When new value is smaller than peak, pop stack until it meets 1), and update the index value to the left-most value.
# Finally, pop all record following 3).
# For instance: [2, 1, 2]
# stack             |           res
# [(2, 0)]          |           0   # (0, 0) is used for avoiding out of index error, ignore it here.
# [(1, 0)]          |           2
# (!!! It is very important to notice that the index value of 1, is actually updated to 0, which is the left most poped record)
# [(1, 0), (2, 2)]  |           2
# [(1, 0)]          |           2
# []                |           3 = max(1 * 3, 2)


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        if len(heights) == 1:
            return heights[0]
        stack = [(0, 0)]  # height and index
        for pos in range(len(heights)):
            if heights[pos] > stack[-1][0]:
                stack.append((heights[pos], pos))
            elif heights[pos] < stack[-1][0]:
                while heights[pos] < stack[-1][0]:
                    last = stack.pop()
                    res = max(res, last[0] * (pos - last[1]))
                stack.append((heights[pos], last[1]))
        while stack:
            last = stack.pop()
            res = max(res, last[0] * (len(heights) - last[1]))
        return res