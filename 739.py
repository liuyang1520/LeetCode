"""
1. Use a queue to append / pop temperatures, get TLE
2. Brute-force, get TLE
3. Revise queue to use a stack, key point is that when append a new record, only need to pop values in the right, no need to go through the whole stack
4. Hash table solution, use a hash to store smallest index of {temprature: index} for the right-side
"""
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        queue, index = [(temperatures[0], 0)], 1
        size = len(temperatures)
        result = [0] * size
        while queue and index < size:
            nextDay = temperatures[index]
            i = 0
            while i < len(queue):
                if nextDay > queue[i][0]:
                    temp = queue.pop(i)
                    result[temp[1]] = index - temp[1]
                    i -= 1
                i += 1
            queue.append([nextDay, index])
            index += 1
        return result

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        size = len(temperatures)
        result = [0] * size
        maxNum = max(temperatures)
        if min(temperatures) == maxNum: return result
        for i in range(size):
            if temperatures[i] == maxNum:
                continue
            for j in range(i, size):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        return result

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack, index = [(temperatures[0], 0)], 1
        size = len(temperatures)
        result = [0] * size
        while stack and index < size:
            nextDay = temperatures[index]
            while stack and stack[-1][0] < nextDay:
                temp = stack.pop()
                result[temp[1]] = index - temp[1]
            stack.append([nextDay, index])
            index += 1
        return result
