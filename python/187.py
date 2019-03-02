# Naive solution. Use set to store strings.
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        map = set()
        res = set()
        if len(s) <= 10:
            return []
        for i in range(0, len(s) - 10 + 1):
            if s[i: i + 10] not in map:
                map.add(s[i: i + 10])
            else:
                if s[i: i + 10] not in res:
                    res.add(s[i: i + 10])
        return list(res)
        

# Find solution online http://bookshadow.com/weblog/2015/02/06/leetcode-repeated-dna-sequences/
# Convert strings to bits, then to numbers, and store them.
# ACGTA = 0001101101
# summation * 4 means move 2 bits to left
# checkDict.get(summation, 0) is a very elegant statement, no need to write key in dict.
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        summation = 0
        checkDict = {}
        map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        res = []
        for i in range(len(s)):
            summation = (summation * 4 + map[s[i]]) & 0xFFFFF
            if i < 9:
                continue
            checkDict[summation] = checkDict.get(summation, 0) + 1
            if checkDict[summation] == 2:
                res.append(s[i-9: i+1])
        return res
