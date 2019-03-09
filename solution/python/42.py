# First find the peak values, and calculate the volume based on different cases.
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        height = [0] + height + [0]
        index = 1
        peaks = []
        while index <= len(height) - 2:
            if height[index - 1] < height[index] and height[index] > height[index + 1]:
                peaks.append(index)
            elif height[index - 1] < height[index] and height[index] == height[index + 1]:
                x = index + 1
                while height[x] == height[index]:
                    x += 1
                if height[x] < height[index]:
                    peaks.append(index)
                else:
                    index = x - 1
            index += 1
        volume = 0
        if len(peaks) < 2:
            return 0
        count = 0
        while count <= len(peaks) - 2:
            endCount = count + 1
            start, end = peaks[count], peaks[endCount]
            if max([height[i] for i in peaks[endCount:]]) >= height[start]:
                while endCount < len(peaks) - 1 and height[start] > height[end]:
                    endCount += 1
                    end = peaks[endCount]
            else:
                maxSubHeight = height[end]
                maxSubHeightIndex = endCount
                for i in range(endCount, len(peaks)):
                    if height[peaks[i]] >= maxSubHeight:
                        maxSubHeight = height[peaks[i]]
                        maxSubHeightIndex = i
                endCount = maxSubHeightIndex
                end = peaks[endCount]
            volume += min(height[start], height[end]) * (end - start - 1)
            for j in range(start + 1, end):
                volume -= min(height[start], height[end], height[j])
            start = end
            count = endCount
        return volume


# A tricky solution. Use a list to store n values for each index i, the left max height before and at i.
# Then use a pointer running from the right side. Add min(leftMaxHeightList[i], rightMaxHeight) - height[i] to the sum.
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftMaxHeightList = [0] * len(height)
        leftMaxHeight = 0
        for i in range(len(height)):
            if height[i] > leftMaxHeight:
                leftMaxHeight = height[i]
            leftMaxHeightList[i] = leftMaxHeight
        volume = 0
        rightMaxHeight = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > rightMaxHeight:
                rightMaxHeight = height[i]
            volume += min(leftMaxHeightList[i], rightMaxHeight) - height[i]
        return volume