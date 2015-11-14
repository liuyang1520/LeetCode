# A very bad implementation. From the lowest bit to the highest bit, compare the sum value to check whether it
# is a new one or not.
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def checkSum(a):
            sum = 0
            for i in range(len(a)):
                    if a[i] == 1:
                        sum += 2 ** i
            return sum
            
        bits = [0] * n
        nums = [0]
        pos = 0
        temp = list(bits)
        while len(nums) < 2 ** n:
            sum = checkSum(bits)
            if sum in nums:
                bits = list(temp)
                if bits[pos] == 0:
                    bits[pos] = 1
                elif bits[pos] == 1:
                    bits[pos] = 0
                pos += 1
                pos %= n
            else:
                nums.append(sum)
                pos = 0
                temp = list(bits)
        return nums


# Found a nice solution online. Transform the binary code into gray code. (x >> 1) ^ x.
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        nums = []
        for i in range(2**n):
            nums.append((i >> 1) ^ i)
        return nums