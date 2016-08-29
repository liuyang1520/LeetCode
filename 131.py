# DFS solution
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(testString):
            if testString == testString[::-1]:
                return True
            return False
        
        def partitionHelper(pos, res):
            if pos == len(s):
                results.append(res)
            for i in range(pos + 1, len(s) + 1):
                if isPalindrome(s[pos: i]):
                    partitionHelper(i, res + [s[pos: i]])

        results = []
        partitionHelper(0, [])
        return results