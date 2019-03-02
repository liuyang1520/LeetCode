"""
Use dictionary to store all possible sums of A and B, C and D, looking for matched results.
Note, to speed up the process, we can directly do:
for i in C:
    for j in D:
        res += sumDict1(-i-j)
Which means we only need one dictionary. This doesn't change the big-O.
"""
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import defaultdict
        
        def enumerateSum(list1, list2):
            sumDict = defaultdict(int)
            for i in list1:
                for j in list2:
                    sumDict[i+j] += 1
            return sumDict
            
        sumDict1 = enumerateSum(A, B)
        sumDict2 = enumerateSum(C, D)
        
        res = 0
        for i in sumDict1:
            if -i in sumDict2:
                res += sumDict1[i] * sumDict2[-i]
        return res