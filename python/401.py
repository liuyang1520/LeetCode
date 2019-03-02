"""
1. use combinations
2. list all possible hour:minute and count how many 1s in it:
    for i in range(12):
        for j in range(60):
            if (bin(i)+bin(j)).count("1") == num:
                append to list
"""
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        from itertools import combinations
        
        def valueLEDs(n, k):
            value = [2**i for i in range(k)]
            coms = combinations(value, n)
            res = []
            for i in coms:
                res += [sum(i)]
            return res
        
        res = []
        for i in range(min(5, num+1)):
            j = num - i
            res4 = valueLEDs(i, 4)
            res6 = valueLEDs(j, 6)
            for p in res4:
                for q in res6:
                    if p < 12 and q < 60:
                        temp = str(q) if q>=10 else "0"+str(q)
                        res.append(str(p) + ":" + temp)
        return sorted(res)