"""
n = 6, k = 4
keep the first 1, 2 from 1, 2, 3, 4, 5, 6
reverse insert the remaining numbers by dividing into two parts: [3, 4] [5, 6] => [6, 3, 5, 4]
combine together: [1, 2, 6, 3, 5, 4]
"""
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = range(1, n+1)[0: n-k]
        temp = range(1, n+1)[n-k:]
        firstHalf, secondHalf = temp[0: (len(temp) / 2)], temp[(len(temp) / 2):][::-1]
        for i in range(k):
            if i % 2 == 0:
                result.append(secondHalf[i/2])
            else:
                result.append(firstHalf[i/2])
            i += 1
        return result
