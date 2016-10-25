"""
Calculate the result in order [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
Should replace counter -= temp with division, to improve the performance
"""
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        Round   1   2   3
        zero    z
        one         o
        two     w
        three       r
        four    u
        five        f
        six     x
        seven       s
        eight   g
        nine            i
        """
        from collections import Counter, defaultdict
        counter = Counter(s)
        numDict = defaultdict(int)
        feature = [("zero", "z"), ("one", "o"), ("two", "w"),
                    ("three", "r"), ("four", "u"), ("five", "f"),
                    ("six", "x"), ("seven", "s"), ("eight", "g"),
                    ("nine", "i")]
        for i in [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]:
            temp = Counter(feature[i][0])
            while counter[feature[i][1]]:
                counter -= temp
                numDict[i] += 1
        res = ""
        for i in range(10):
            res += str(i) * numDict[i]
        return res