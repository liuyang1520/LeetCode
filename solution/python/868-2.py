class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = bin(N)[2:]
        maxLength = 0
        lastIndex = float('inf')
        for i in range(len(binary)):
            if binary[i] == '1':
                maxLength = max(i - lastIndex, maxLength)
                lastIndex = i
        return maxLength
